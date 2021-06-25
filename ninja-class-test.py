class Job:

    def __init__(self):
        self.jobName = input("Enter Job Name: ")
        self.jobDesc = input("Enter Job Description: ")
        self.jobHours = input("Enter Job required hours: ")

    def do_work(self):
        print(f"{self.jobName} {self.jobDesc} {self.jobHours}")


class Programmer(Job):
    pass

class Pilot(Job):
    pass


if __name__ == "__main__":
    myJob = Job()
    myJob.do_work()
