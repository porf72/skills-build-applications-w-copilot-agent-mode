from django.core.management.base import BaseCommand
from django.conf import settings
from pymongo import MongoClient, ASCENDING

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient(host='localhost', port=27017)
        db = client['octofit_db']

        # Drop collections if exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Teams
        teams = [
            {'_id': 1, 'name': 'Marvel'},
            {'_id': 2, 'name': 'DC'}
        ]
        db.teams.insert_many(teams)

        # Users (supereroi)
        users = [
            {'_id': 1, 'name': 'Spider-Man', 'email': 'spiderman@marvel.com', 'team_id': 1},
            {'_id': 2, 'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team_id': 1},
            {'_id': 3, 'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team_id': 2},
            {'_id': 4, 'name': 'Batman', 'email': 'batman@dc.com', 'team_id': 2}
        ]
        db.users.insert_many(users)
        db.users.create_index([('email', ASCENDING)], unique=True)

        # Activities
        activities = [
            {'_id': 1, 'user_id': 1, 'type': 'run', 'distance': 5},
            {'_id': 2, 'user_id': 2, 'type': 'cycle', 'distance': 20},
            {'_id': 3, 'user_id': 3, 'type': 'swim', 'distance': 2},
            {'_id': 4, 'user_id': 4, 'type': 'run', 'distance': 10}
        ]
        db.activities.insert_many(activities)

        # Workouts
        workouts = [
            {'_id': 1, 'user_id': 1, 'workout': 'Push-ups', 'reps': 30},
            {'_id': 2, 'user_id': 2, 'workout': 'Sit-ups', 'reps': 40},
            {'_id': 3, 'user_id': 3, 'workout': 'Squats', 'reps': 50},
            {'_id': 4, 'user_id': 4, 'workout': 'Pull-ups', 'reps': 20}
        ]
        db.workouts.insert_many(workouts)

        # Leaderboard
        leaderboard = [
            {'_id': 1, 'user_id': 1, 'points': 100},
            {'_id': 2, 'user_id': 2, 'points': 90},
            {'_id': 3, 'user_id': 3, 'points': 110},
            {'_id': 4, 'user_id': 4, 'points': 95}
        ]
        db.leaderboard.insert_many(leaderboard)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data!'))
