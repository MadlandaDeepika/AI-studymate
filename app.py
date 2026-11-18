
import streamlit as st
from pathlib import Path

# -----------------------------------
# PAGE CONFIGURATION
# -----------------------------------

st.set_page_config(
    page_title="AI StudyMate",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------
# LOAD CUSTOM CSS
# -----------------------------------

css_file = Path(__file__).parent / "style.css"

if css_file.exists():
    with open(css_file, "r", encoding="utf-8") as file:
        st.markdown(
            f"<style>{file.read()}</style>",
            unsafe_allow_html=True
        )

# -----------------------------------
# SESSION STATE
# -----------------------------------

if "uploaded_file" not in st.session_state:
    st.session_state["uploaded_file"] = None

if "uploaded_file_name" not in st.session_state:
    st.session_state["uploaded_file_name"] = None

if "study_started" not in st.session_state:
    st.session_state["study_started"] = False

# -----------------------------------
# SIDEBAR NAVIGATION
# -----------------------------------

with st.sidebar:

    st.title("🌿 AI StudyMate")

    st.caption("Your personal AI-powered study companion")

    st.write("---")

    page = st.radio(
        "Navigation",
        [
            "Home",
            "Upload Notes",
            "AI Summary",
            "MCQ Practice",
            "Interactive Quiz",
            "Quiz Results"
        ]
    )

    st.write("---")

    st.caption("Learn smarter. Grow every day. 🌱")


# ===================================
# HOME PAGE
# ===================================

if page == "Home":

    st.title("A little progress, every day. 🌱")

    st.write(
        "Welcome to AI StudyMate — your personal learning "
        "space to understand, practise, and improve."
    )

    st.write("")

    with st.container(border=True):

        st.subheader("Welcome to your learning space! 🌿")

        st.write(
            "Upload your study materials and let AI help you "
            "turn complex notes into simpler learning."
        )

        st.write("")

        st.markdown("**Your learning journey starts here.**")

        st.caption(
            "Upload notes → Understand concepts → Practise questions → "
            "Test yourself → Improve"
        )

    st.write("")

    st.subheader("Explore your learning tools")

    col1, col2 = st.columns(2)

    with col1:

        with st.container(border=True):

            st.markdown("### 📖 Smart Summary")

            st.write(
                "Turn lengthy study materials into "
                "simple and understandable summaries."
            )

        with st.container(border=True):

            st.markdown("### 🧠 MCQ Practice")

            st.write(
                "Practise important multiple-choice "
                "questions generated from your notes."
            )

    with col2:

        with st.container(border=True):

            st.markdown("### 🎯 Interactive Quiz")

            st.write(
                "Test your knowledge through an "
                "interactive quiz experience."
            )

        with st.container(border=True):

            st.markdown("### 📊 Learning Progress")

            st.write(
                "Review your performance and identify "
                "topics that need more attention."
            )


# ===================================
# UPLOAD NOTES PAGE
# ===================================

elif page == "Upload Notes":

    st.title("Your learning starts here. 🌿")

    st.write(
        "Bring your study materials. We'll help you turn them "
        "into clearer, smarter learning."
    )

    st.write("")

    with st.container(border=True):

        st.markdown("### 📂 Upload your study material")

        st.write(
            "Choose your notes in PDF or TXT format "
            "to begin your learning session."
        )

        uploaded_file = st.file_uploader(
            "Drop your file here or browse files",
            type=["pdf", "txt"],
            accept_multiple_files=False,
            key="study_material"
        )

        st.caption("Supported formats: PDF and TXT")

        if uploaded_file is not None:

            file_size = uploaded_file.size / 1024

            st.success("Your study material is ready!")

            col1, col2 = st.columns(2)

            with col1:

                st.markdown("**📄 File name**")
                st.write(uploaded_file.name)

            with col2:

                st.markdown("**📦 File size**")
                st.write(f"{file_size:.2f} KB")

            if st.button(
                "🌱 Start Studying",
                use_container_width=True
            ):

                st.session_state["uploaded_file"] = uploaded_file
                st.session_state["uploaded_file_name"] = uploaded_file.name
                st.session_state["study_started"] = True

                st.success(
                    "Your file is saved for this study session! "
                    "AI processing will be connected during integration."
                )

        else:

            st.info(
                "No file selected yet. Upload your notes "
                "when you're ready."
            )

    st.write("")

    st.subheader("What happens next?")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("### 📖")
        st.markdown("**Understand**")
        st.caption("Get simplified AI summaries.")

    with col2:

        st.markdown("### 🧠")
        st.markdown("**Practise**")
        st.caption("Generate questions from your notes.")

    with col3:

        st.markdown("### 🎯")
        st.markdown("**Improve**")
        st.caption("Test yourself and review your progress.")


# ===================================
# AI SUMMARY PAGE
# ===================================

elif page == "AI Summary":

    st.title("Understand your notes, effortlessly. 🌿")

    st.write(
        "A clearer way to explore the important ideas "
        "in your study material."
    )

    st.write("")

    summary = st.session_state.get("summary_text")

    key_points = st.session_state.get("key_points", [])

    document_name = st.session_state.get(
        "uploaded_file_name",
        "Your study material"
    )

    if summary:

        with st.container(border=True):

            st.markdown("### 📄 Study document")

            st.write(document_name)

            st.success("AI summary is ready!")

        st.write("")

        st.subheader("Your summary")

        with st.container(border=True):

            st.markdown(summary)

        st.write("")

        st.subheader("Key takeaways")

        if key_points:

            for index, point in enumerate(key_points, start=1):

                with st.container(border=True):

                    st.markdown(f"**{index}. {point}**")

        else:

            st.info("Key points will appear here.")

        st.download_button(
            label="📥 Download Summary",
            data=summary,
            file_name="AI_StudyMate_Summary.txt",
            mime="text/plain",
            use_container_width=True
        )

    else:

        with st.container(border=True):

            st.markdown("### 📖 Your learning space is ready")

            st.write(
                "Once your notes are processed by AI, "
                "your simplified summary will appear here."
            )

            st.write("")

            col1, col2, col3 = st.columns(3)

            with col1:

                st.markdown("### ✨")
                st.markdown("**Simplified concepts**")
                st.caption("Understand difficult topics.")

            with col2:

                st.markdown("### 💡")
                st.markdown("**Key takeaways**")
                st.caption("Focus on important information.")

            with col3:

                st.markdown("### 📚")
                st.markdown("**Easy revision**")
                st.caption("Review your material anytime.")

        st.info(
            "Your AI-generated summary will be available "
            "after your study material is processed."
        )


# ===================================
# MCQ PRACTICE PAGE
# ===================================

elif page == "MCQ Practice":

    st.title("Learn through practice. 🧠")

    st.write(
        "Strengthen your understanding with questions "
        "created from your study material."
    )

    st.write("")

    questions = st.session_state.get("mcq_questions", [])

    if questions:

        st.success(
            f"{len(questions)} questions are ready for practice!"
        )

        for index, question in enumerate(questions, start=1):

            with st.container(border=True):

                st.markdown(f"### Question {index}")

                st.write(question["question"])

                for option in question["options"]:

                    st.write(f"○  {option}")

                if question.get("explanation"):

                    with st.expander("View explanation"):

                        st.write(question["explanation"])

    else:

        with st.container(border=True):

            st.markdown("### 🌱 Your practice space is ready")

            st.write(
                "Once AI generates questions from your notes, "
                "they will appear here."
            )

            st.write("")

            col1, col2, col3 = st.columns(3)

            with col1:

                st.markdown("### 🎯")
                st.markdown("**Test yourself**")
                st.caption("Check your understanding.")

            with col2:

                st.markdown("### 🧠")
                st.markdown("**Think better**")
                st.caption("Practise important concepts.")

            with col3:

                st.markdown("### 📚")
                st.markdown("**Revise smarter**")
                st.caption("Learn from every question.")

        st.info(
            "Your AI-generated MCQs will appear here "
            "after your notes are processed."
        )


# ===================================
# INTERACTIVE QUIZ PAGE
# ===================================

elif page == "Interactive Quiz":

    st.title("Challenge yourself. 🎯")

    st.write(
        "Put your understanding to the test "
        "with an interactive learning experience."
    )

    st.write("")

    with st.container(border=True):

        st.markdown("### 🧠 Your quiz space")

        st.write(
            "Your questions will appear here once "
            "your study material is processed."
        )

        st.write("")

        st.markdown("**Your quiz journey**")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.markdown("### 01")
            st.markdown("**Read**")
            st.caption("Understand each question.")

        with col2:

            st.markdown("### 02")
            st.markdown("**Answer**")
            st.caption("Choose the correct option.")

        with col3:

            st.markdown("### 03")
            st.markdown("**Review**")
            st.caption("Learn from your results.")

    st.info(
        "Interactive questions and answer selection "
        "will be connected during integration."
    )


# ===================================
# QUIZ RESULTS PAGE
# ===================================

elif page == "Quiz Results":

    st.title("Every step is progress. 🌱")

    st.write(
        "Review your performance, understand your mistakes, "
        "and keep improving."
    )

    st.write("")

    results = st.session_state.get("quiz_results")

    if results:

        with st.container(border=True):

            st.markdown("### 🏆 Your performance")

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "Total Questions",
                    results.get("total", 0)
                )

            with col2:

                st.metric(
                    "Correct Answers",
                    results.get("correct", 0)
                )

            with col3:

                st.metric(
                    "Wrong Answers",
                    results.get("wrong", 0)
                )

            st.write("")

            st.metric(
                "Your Score",
                f'{results.get("score", 0)}%'
            )

        st.write("")

        st.subheader("Your learning review")

        with st.container(border=True):

            st.markdown("### 💡 Areas to improve")

            st.write(
                results.get(
                    "suggestions",
                    "Your revision suggestions will appear here."
                )
            )

    else:

        with st.container(border=True):

            st.markdown("### 📊 Your progress will appear here")

            st.write(
                "Complete an interactive quiz to see your "
                "score, correct answers, and areas for improvement."
            )

            st.write("")

            col1, col2, col3 = st.columns(3)

            with col1:

                st.markdown("### 🏆")
                st.markdown("**Your score**")
                st.caption("See how well you performed.")

            with col2:

                st.markdown("### 📖")
                st.markdown("**Answer review**")
                st.caption("Understand your mistakes.")

            with col3:

                st.markdown("### 🌱")
                st.markdown("**Improve**")
                st.caption("Find topics to revise.")

        st.info(
            "Your results will appear here after completing a quiz."
        )
