from dotenv import load_dotenv
from modules.clock_in_out.scheduler import main as clock_in_out_scheduler

load_dotenv()

if __name__ == "__main__":
    clock_in_out_scheduler()

