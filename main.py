import sys
from logger import Logger
from query_generator import Generateai
log = Logger.get_logs("Main")

class Main:

    def test_ai(self):
        try:
            user_text = input("Enter your query:")
            q_b = Generateai()
            output = q_b.generate_query(user_text)
            log.info(f"{user_text}-->{output}")
        except:
            exc_type, exc_msg, exc_line = sys.exc_info()
            log.info(f"{exc_type} at {exc_line.tb_lineno} as {exc_msg}")
if __name__ == "__main__":
    m_b = Main()
    m_b.test_ai()