from dotenv import load_dotenv
from modules import clock_in_out


load_dotenv()

if __name__ == "__main__":
    clock_in_out.scheduler.main()

