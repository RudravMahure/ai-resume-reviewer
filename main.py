import streamlit as st

from file_processor import extract_text
from llm import review_resume

st.set_page_config(
    page_title="AI Resume Reviewer",
    page_icon="📄",
    layout="wide"
)

st.title("AI Resume Reviewer")

st.write(
    "Upload your resume and get AI-powered feedback"
    "on your resume"
)

uploaded_file = st.file_uploader(
    "Upload your resume",
    type=["pdf", "docx"]
)

if uploaded_file:

    st.success(
        f"Uploaded: {uploaded_file.name}"
    )
    
    if st.button("🔍 Review Resume"):
        
        with st.spinner("Analyzing your resume..."):
            
            try:
                resume_text = extract_text(
                    uploaded_file
                )
                
                if not resume_text.strip():
                    st.error(
                        "Could not extract text from the resume"
                    )
                
                else:
                    
                    review = review_resume(
                        resume_text
                    )
                    
                    st.success(
                        "Resume analysis completed!"
                    )
                    
                    st.subheader(
                        "📊 Resume Score"
                    )
                    
                    col1,col2 = st.columns(2)
                    
                    with col1:(
                        st.metric(
                            "Overall Score",
                            f"{review.overall_score}/100"
                        )
                    )
                    
                    with col2:(
                        st.metric(
                            "ATS Score",
                            f"{review.ats_score}/100"
                        )
                    )
                    
                    st.subheader(
                        "📝 Summary"
                    )
                    
                    st.write(
                        review.summary
                    )

                    st.subheader(
                        "💪 Strengths"
                    )

                    for strength in review.strengths:
                        st.write(
                            f"✅ {strength}"
                        )

                    st.subheader(
                        "⚠️ Areas to Improve"
                    )

                    for weakness in review.weaknesses:
                        st.write(
                            f"⚠️ {weakness}"
                        )

                    st.subheader(
                        "💡 Suggestions"
                    )
                    
                    for suggestion in review.suggestions:
                        st.write(
                            f"💡 {suggestion}"
                    )
                
            except Exception as e:
                
                st.error(
                    f"Something went wrong: {e}"
                )    