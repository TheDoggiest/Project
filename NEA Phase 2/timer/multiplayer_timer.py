# timer/multiplayer_timer.py
from timer.timer_manager import TimerManager

class MultiplayerTimer:
    def __init__(self, players: list):
        self.players = players  # list of player names or IDs
        self.timers = {player: TimerManager() for player in players}
        self.completed_times = {}

    def start_timer(self, player):
        if player in self.timers:
            self.timers[player].start()

    def stop_timer(self, player):
        if player in self.timers:
            self.timers[player].stop()
            self.completed_times[player] = self.timers[player].get_duration()

    def get_player_time(self, player):
        return self.timers[player].get_duration_str()

    def get_winner(self):
        if not self.completed_times:
            return None
        return min(self.completed_times, key=self.completed_times.get)

    def get_all_times(self):
        return {
            player: self.timers[player].get_duration_str()
            for player in self.players
        }
