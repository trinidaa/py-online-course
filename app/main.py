class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        if weeks < 0:
            raise ValueError("Initial weeks cannot be negative")

        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        if days < 0:
            raise ValueError("Days cannot be negative")

        total_weeks = days // 7
        if days % 7 == 0:
            return total_weeks
        else:
            return total_weeks + 1

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        name = course_dict.get("name")
        description = course_dict.get("description")
        days = course_dict.get("days", 0)

        total_weeks = cls.days_to_weeks(days)
        return cls(name, description, total_weeks)
