from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Users
        ironman = User.objects.create(email='ironman@marvel.com', name='Iron Man', team='Marvel', is_superhero=True)
        captain = User.objects.create(email='captain@marvel.com', name='Captain America', team='Marvel', is_superhero=True)
        batman = User.objects.create(email='batman@dc.com', name='Batman', team='DC', is_superhero=True)
        superman = User.objects.create(email='superman@dc.com', name='Superman', team='DC', is_superhero=True)

        # Activities
        Activity.objects.create(user=ironman.email, type='Running', duration=30, date='2025-11-01')
        Activity.objects.create(user=batman.email, type='Cycling', duration=45, date='2025-11-02')

        # Leaderboard
        Leaderboard.objects.create(team='Marvel', points=100)
        Leaderboard.objects.create(team='DC', points=120)

        # Workouts
        Workout.objects.create(name='Hero HIIT', description='High intensity for heroes', difficulty='Hard')
        Workout.objects.create(name='Sidekick Cardio', description='Cardio for sidekicks', difficulty='Medium')

        self.stdout.write(self.style.SUCCESS('Database populated successfully.'))
