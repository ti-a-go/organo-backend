import requests, json
from http.client import responses


def main():
    teams = [
        {"name": "Front-End", "primary_color": "#82CFFA", "secondary_color": "#E8F8FF"},
        {
            "name": "Data Science",
            "primary_color": "#A6D157",
            "secondary_color": "#F0F8E2",
        },
        {"name": "Devops", "primary_color": "#E06B69", "secondary_color": "#FDE7E8"},
        {
            "name": "UX e Design",
            "primary_color": "#D86EBF",
            "secondary_color": "#FAE5F5",
        },
        {"name": "Mobile", "primary_color": "#FEBA05", "secondary_color": "#FFF5D9"},
        {
            "name": "Inovação e Gestão",
            "primary_color": "#FF8A29",
            "secondary_color": "#FFEEDF",
        },
    ]

    for team in teams:
        response = requests.post("http://localhost:8000/teams", json.dumps(team))
        print(f"{team["name"]}: {response.status_code} - {responses[response.status_code]}")


if __name__ == "__main__":
    main()
