import streamlit as st
from services.deepseek_service import DeepSeekTool
from rich.traceback import install
install(show_locals=True)

def process_text_with_deepseek(api_key: str, user: str, password: str, input_text: str, instruction: str) -> str:
    """Process text using DeepSeek API with error handling."""
    try:
        tool = DeepSeekTool(api_key, user, password)
        result = tool.process_text(input_text, instruction)
        if not result:
            raise ValueError("Empty response received from DeepSeek")
        return result
    except Exception as e:
        raise Exception(f"Processing failed: {str(e)}")

def render_text_input() -> tuple[str, bool]:
    """Handle text input methods and return the input text and its validity."""
    uploaded_file = st.file_uploader("Choose a text file", type=['txt'])
    
    if uploaded_file:
        try:
            input_text = uploaded_file.getvalue().decode('utf-8')
            st.text_area("File Content", input_text, height=200, disabled=True)
            return input_text, True
        except Exception as e:
            st.error(f"Error reading file: {str(e)}")
            return "", False
    
    return st.text_area("Or paste your text here", height=200), True

def main():
    # Page configuration
    st.set_page_config(
        page_title="DeepSeek Prompt Tester",
        page_icon="📝",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    st.title("DeepSeek Prompt Tester")

    # Get credentials directly from secrets
    api_key = st.secrets["DEEPSEEK_API_KEY"]
    user = st.secrets["DEEPSEEK_USER"]
    password = st.secrets["DEEPSEEK_PASSWORD"]

    if not all([api_key, user, password]):
        st.error("⚠️ Credentials not found in secrets")
        st.stop()

    # Get input text and validate
    input_text, is_valid = render_text_input()
    
    # Get instruction
    instruction = st.text_area("Enter your instruction/prompt", 
                             height=100,
                             placeholder="Enter your instructions here...")

    # Process text when conditions are met
    if st.button("Process Text", type="primary"):
        if not is_valid:
            st.error("Please provide valid input text")
            return
        
        if not instruction:
            st.error("Please provide processing instructions")
            return
            
        if not input_text:
            st.error("Please provide input text")
            return

        with st.spinner("Processing your text..."):
            try:
                result = process_text_with_deepseek(api_key, user, password, input_text, instruction)
                st.success("✨ Processing complete!")
                
                with st.expander("Show Result", expanded=True):
                    st.markdown("### Result")
                    st.markdown(result)
                    
                    # Add copy button for result
                    st.button("Copy Result", 
                             on_click=lambda: st.write(result))
                    
            except Exception as e:
                st.error(f"❌ {str(e)}")

if __name__ == "__main__":
    main()
