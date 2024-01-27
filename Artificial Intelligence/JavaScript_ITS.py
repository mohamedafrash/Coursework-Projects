import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QStackedWidget, QProgressBar, QTextEdit
from PyQt5.QtGui import QFont, QColor

class HomePage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet("background-color: #fcd000;")  # Set background color to yellow

        welcome_label = QLabel("Welcome to the Intelligent Tutoring System for JavaScript Learning")
        intro_label = QLabel("Choose an option to begin your learning journey:")
        welcome_label.setFont(QFont("Arial", 20, QFont.Bold))  # Larger and bold font for welcome label

        learning_path_btn = self.create_button("Learning Path", "Start a personalized learning path based on your skill level and interests", self.show_learning_path)
        topics_btn = self.create_button("Topics", "Explore specific JavaScript topics, such as Core JavaScript, DOM Manipulation, and Asynchronous Programming", self.show_topics)
        resources_btn = self.create_button("Learning Resources", "Access a variety of learning resources, including tutorials, videos, documentation, and interactive exercises", self.show_resources)
        assessments_btn = self.create_button("Assessments", "Take quizzes and coding challenges to assess your understanding of JavaScript concepts", self.show_assessments)
        feedback_btn = self.create_button("Feedback", "Receive personalized feedback on your performance and progress", self.show_feedback)

        layout = QVBoxLayout(self)
        layout.addWidget(welcome_label)
        layout.addWidget(intro_label)
        layout.addWidget(learning_path_btn)
        layout.addWidget(topics_btn)
        layout.addWidget(resources_btn)
        layout.addWidget(assessments_btn)
        layout.addWidget(feedback_btn)

        learning_path_btn.clicked.connect(self.show_learning_path)
        topics_btn.clicked.connect(self.show_topics)
        resources_btn.clicked.connect(self.show_resources)
        assessments_btn.clicked.connect(self.show_assessments)
        feedback_btn.clicked.connect(self.show_feedback)

    def show_learning_path(self):
        self.stacked_widget.setCurrentIndex(1)  # Switch to the Learning Path page

    def show_topics(self):
        self.stacked_widget.setCurrentIndex(2)  # Switch to the Topics page

    def show_resources(self):
        self.stacked_widget.setCurrentIndex(3)  # Switch to the Learning Resources page

    def show_assessments(self):
        self.stacked_widget.setCurrentIndex(4)  # Switch to the Assessments page

    def show_feedback(self):
        self.stacked_widget.setCurrentIndex(5)  # Switch to the Feedback page    

    def create_button(self, text, tooltip, click_function):
        button = QPushButton(text)
        button.setToolTip(tooltip)
        button.clicked.connect(click_function)
        self.style_button(button, QColor(0, 0, 0))  # Black color
        return button


    def style_button(self, button, color):
        button.setStyleSheet(
            f"QPushButton {{ background-color: {color.name()}; color: yellow; font-weight: bold; padding: 10px; border-radius: 5px; }}"
            "QPushButton:hover { background-color: #333; }"
        )

    def show_page(self):
        sender_button = self.sender()
        if sender_button.text() == "Learning Path":
            self.stacked_widget.setCurrentIndex(1)  # Change the index to the corresponding page

class LearningPathPage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet("background-color: #fcd000;")  # Set background color to yellow

        title_label = QLabel("Learning Path")
        title_label.setFont(QFont("Arial", 20, QFont.Bold))  # Larger and bold font for the title

        description_label = QLabel("Follow the learning path to enhance your JavaScript skills.")
        description_label.setFont(QFont("Arial", 14))

        progress_label = QLabel("Your Progress:")
        progress_bar = QProgressBar()

        current_topic_label = QLabel("Current Topic: JavaScript Basics")
        next_topic_label = QLabel("Next Topic: DOM Manipulation")

        next_button = self.create_button("Next", "Go to the next topic")
        back_button = self.create_button("Back", "Return to the homepage")

        layout = QVBoxLayout(self)
        layout.addWidget(title_label)
        layout.addWidget(description_label)
        layout.addWidget(progress_label)
        layout.addWidget(progress_bar)
        layout.addWidget(current_topic_label)
        layout.addWidget(next_topic_label)
        layout.addWidget(next_button)
        layout.addWidget(back_button)

    def create_button(self, text, tooltip):
        button = QPushButton(text)
        button.setToolTip(tooltip)
        button.clicked.connect(self.show_page)
        self.style_button(button, QColor(0, 0, 0))  # Black color
        return button

    def style_button(self, button, color):
        button.setStyleSheet(
            f"QPushButton {{ background-color: {color.name()}; color: yellow; font-weight: bold; padding: 10px; border-radius: 5px; }}"
            "QPushButton:hover { background-color: #333; }"
        )

    def show_page(self):
        sender_button = self.sender()
        if sender_button.text() == "Back":
            self.stacked_widget.setCurrentIndex(0)  # Return to the homepage

class TopicsPage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet("background-color: #fcd000;")  # Set background color to yellow

        title_label = QLabel("JavaScript Topics")
        title_label.setFont(QFont("Arial", 20, QFont.Bold))  # Larger and bold font for the title

        description_label = QLabel("Explore specific JavaScript topics to deepen your understanding.")
        description_label.setFont(QFont("Arial", 14))

        topic1_btn = self.create_button("Core JavaScript", "Explore fundamental JavaScript concepts")
        topic2_btn = self.create_button("DOM Manipulation", "Learn how to manipulate the Document Object Model")
        topic3_btn = self.create_button("Asynchronous Programming", "Understand asynchronous programming in JavaScript")

        next_button = self.create_button("Next", "Go to the next topic")
        back_button = self.create_button("Back", "Return to the homepage")

        layout = QVBoxLayout(self)
        layout.addWidget(title_label)
        layout.addWidget(description_label)
        layout.addWidget(topic1_btn)
        layout.addWidget(topic2_btn)
        layout.addWidget(topic3_btn)
        layout.addWidget(next_button)
        layout.addWidget(back_button)

    def create_button(self, text, tooltip):
        button = QPushButton(text)
        button.setToolTip(tooltip)
        button.clicked.connect(self.show_page)
        self.style_button(button, QColor(0, 0, 0))  # Black color
        return button

    def style_button(self, button, color):
        button.setStyleSheet(
            f"QPushButton {{ background-color: {color.name()}; color: yellow; font-weight: bold; padding: 10px; border-radius: 5px; }}"
            "QPushButton:hover { background-color: #333; }"
        )

    def show_page(self):
        sender_button = self.sender()
        if sender_button.text() == "Next":
            self.stacked_widget.setCurrentIndex(2)  # Go to the next page (Learning Resources, adjust index as needed)
        elif sender_button.text() == "Back":
            self.stacked_widget.setCurrentIndex(0)  # Return to the homepage
        # Add conditions for other buttons/pages here

class LearningResourcesPage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet("background-color: #fcd000;")  # Set background color to yellow

        title_label = QLabel("Learning Resources")
        title_label.setFont(QFont("Arial", 20, QFont.Bold))  # Larger and bold font for the title

        description_label = QLabel("Access a variety of learning resources to enhance your JavaScript skills.")
        description_label.setFont(QFont("Arial", 14))

        tutorial_btn = self.create_button("Tutorials", "Explore interactive tutorials for hands-on learning")
        video_btn = self.create_button("Videos", "Watch educational videos to understand JavaScript concepts")
        documentation_btn = self.create_button("Documentation", "Refer to official documentation for in-depth information")
        exercises_btn = self.create_button("Interactive Exercises", "Practice coding with interactive exercises")

        next_button = self.create_button("Next", "Go to the next topic")
        back_button = self.create_button("Back", "Return to the homepage")

        layout = QVBoxLayout(self)
        layout.addWidget(title_label)
        layout.addWidget(description_label)
        layout.addWidget(tutorial_btn)
        layout.addWidget(video_btn)
        layout.addWidget(documentation_btn)
        layout.addWidget(exercises_btn)
        layout.addWidget(next_button)
        layout.addWidget(back_button)

    def create_button(self, text, tooltip):
        button = QPushButton(text)
        button.setToolTip(tooltip)
        button.clicked.connect(self.show_page)
        self.style_button(button, QColor(0, 0, 0))  # Black color
        return button

    def style_button(self, button, color):
        button.setStyleSheet(
            f"QPushButton {{ background-color: {color.name()}; color: yellow; font-weight: bold; padding: 10px; border-radius: 5px; }}"
            "QPushButton:hover { background-color: #333; }"
        )

    def show_page(self):
        sender_button = self.sender()
        if sender_button.text() == "Next":
            self.stacked_widget.setCurrentIndex(3)  # Go to the next page (Assessments, adjust index as needed)
        elif sender_button.text() == "Back":
            self.stacked_widget.setCurrentIndex(0)  # Return to the homepage
        # Add conditions for other buttons/pages here

class AssessmentsPage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet("background-color: #fcd000;")  # Set background color to yellow

        title_label = QLabel("Assessments")
        title_label.setFont(QFont("Arial", 20, QFont.Bold))  # Larger and bold font for the title

        description_label = QLabel("Take quizzes and coding challenges to assess your understanding of JavaScript concepts.")
        description_label.setFont(QFont("Arial", 14))

        quiz_btn = self.create_button("Quizzes", "Test your knowledge with quizzes")
        coding_challenge_btn = self.create_button("Coding Challenges", "Solve coding challenges to apply your skills")

        next_button = self.create_button("Next", "Go to the next topic")
        back_button = self.create_button("Back", "Return to the homepage")

        layout = QVBoxLayout(self)
        layout.addWidget(title_label)
        layout.addWidget(description_label)
        layout.addWidget(quiz_btn)
        layout.addWidget(coding_challenge_btn)
        layout.addWidget(next_button)
        layout.addWidget(back_button)

    def create_button(self, text, tooltip):
        button = QPushButton(text)
        button.setToolTip(tooltip)
        button.clicked.connect(self.show_page)
        self.style_button(button, QColor(0, 0, 0))  # Black color
        return button

    def style_button(self, button, color):
        button.setStyleSheet(
            f"QPushButton {{ background-color: {color.name()}; color: yellow; font-weight: bold; padding: 10px; border-radius: 5px; }}"
            "QPushButton:hover { background-color: #333; }"
        )

    def show_page(self):
        sender_button = self.sender()
        if sender_button.text() == "Next":
            self.stacked_widget.setCurrentIndex(4)  # Go to the next page (Feedback, adjust index as needed)
        elif sender_button.text() == "Back":
            self.stacked_widget.setCurrentIndex(0)  # Return to the homepage

class FeedbackPage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet("background-color: #fcd000;")  # Set background color to yellow

        title_label = QLabel("Feedback")
        title_label.setFont(QFont("Arial", 20, QFont.Bold))  # Larger and bold font for the title

        description_label = QLabel("Receive personalized feedback on your performance and progress.")
        description_label.setFont(QFont("Arial", 14))

        feedback_label = QLabel("Provide your feedback:")
        feedback_text_edit = QTextEdit()

        advice_label = QLabel("Personalized advice and recommendations:")
        advice_text_edit = QTextEdit()

        submit_button = self.create_button("Submit", "Submit your feedback")
        back_button = self.create_button("Back", "Return to the homepage")

        layout = QVBoxLayout(self)
        layout.addWidget(title_label)
        layout.addWidget(description_label)
        layout.addWidget(feedback_label)
        layout.addWidget(feedback_text_edit)
        layout.addWidget(advice_label)
        layout.addWidget(advice_text_edit)
        layout.addWidget(submit_button)
        layout.addWidget(back_button)

    def create_button(self, text, tooltip):
        button = QPushButton(text)
        button.setToolTip(tooltip)
        button.clicked.connect(self.show_page)
        self.style_button(button, QColor(0, 0, 0))  # Black color
        return button

    def style_button(self, button, color):
        button.setStyleSheet(
            f"QPushButton {{ background-color: {color.name()}; color: yellow; font-weight: bold; padding: 10px; border-radius: 5px; }}"
            "QPushButton:hover { background-color: #333; }"
        )

    def show_page(self):
        sender_button = self.sender()
        if sender_button.text() == "Back":
            self.stacked_widget.setCurrentIndex(0)  # Return to the homepage
        # Add conditions for other buttons/pages here

class MainApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.stacked_widget = QStackedWidget(self)
        self.setup_pages()
        self.setCentralWidget(self.stacked_widget)
        self.setWindowTitle('JavaScript Learning ITS')

    def setup_pages(self):
        # Create instances of each page and add them to the stacked widget
        home_page = HomePage(self.stacked_widget)
        learning_path_page = LearningPathPage(self.stacked_widget)
        topics_page = TopicsPage(self.stacked_widget)
        learning_resources_page = LearningResourcesPage(self.stacked_widget)
        assessments_page = AssessmentsPage(self.stacked_widget)
        feedback_page = FeedbackPage(self.stacked_widget)

        self.stacked_widget.addWidget(home_page)
        self.stacked_widget.addWidget(learning_path_page)
        self.stacked_widget.addWidget(topics_page)
        self.stacked_widget.addWidget(learning_resources_page)
        self.stacked_widget.addWidget(assessments_page)
        self.stacked_widget.addWidget(feedback_page)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_app = MainApplication()
    main_app.show()
    sys.exit(app.exec_())
