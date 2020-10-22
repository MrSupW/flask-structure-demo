from .user_blue import user_blue
from .student_blue import student_blue
from .main_blue import main_blue


def init_view(app):
    app.register_blueprint(user_blue)
    app.register_blueprint(student_blue)
    app.register_blueprint(main_blue)
