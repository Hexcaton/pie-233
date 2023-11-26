def get_user_data():
    first_name = input("First name: ")
    surname = input("SURNAME: ")
    objective = input("Objective: ")

    education_degree = input("Education Degree: ")
    education_dates = input("Education Dates from to: ")

    experience_job_title = input("Experience Job Title: ")
    experience_dates = input("Experience Dates from to: ")

    return {
        "First Name": first_name,
        "Surname": surname,
        "Objective": objective,
        "Education Degree": education_degree,
        "Education Dates": education_dates,
        "Experience Job Title": experience_job_title,
        "Experience Dates": experience_dates
    }

def main():
    user_data = get_user_data()

    print("\n===== Resume =====")
    for key, value in user_data.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
