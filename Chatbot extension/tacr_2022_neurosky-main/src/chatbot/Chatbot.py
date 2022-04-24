from src.chatbot.ChatbotDatabase import ChatbotDatabase
from random import randrange
from datetime import datetime, timedelta


class Chatbot:
    def __init__(self, textbox, pn):
        self.textbox = textbox
        self.attention = None
        self.task_step = 0
        self.time_to_idle = timedelta(seconds=20)
        self.time_to_fail = timedelta(seconds=40)
        self.time = datetime.now()
        self.time_difference = (datetime.now() - self.time)
        self.is_idle = False

        self.intro()

        pn.set_status_callback(self.on_status_changed)
        pn.set_attention_callback(self.on_attention_changed)
        pn.set_meditation_callback(self.on_meditation_changed)
        pn.set_blinkStrength_callback(self.on_blinkStrengh_changed)

    def write_message_from_database(self, database):
        return self.textbox.append(database[randrange(0, len(database))]+"\n")

    def on_status_changed(self, status):
        if status == "connected":
            self.write_message_from_database(ChatbotDatabase.after_connection_messages)

        elif status == "NotConnected":
            self.write_message_from_database(ChatbotDatabase.headband_was_turned_off_messages)

    def on_attention_changed(self, attention):
        if self.attention is None:
            self.write_message_from_database(ChatbotDatabase.after_connection_messages)
            self.write_message_from_database(ChatbotDatabase.first_task_messages)
            self.time = datetime.now()

        self.attention = attention
        self.time_difference = (datetime.now() - self.time)

        if self.task_step == 1:
            self.task_one(attention)

    def on_meditation_changed(self, meditation):
        self.time_difference = (datetime.now() - self.time)

        if self.task_step == 2:
            self.task_two(meditation)

    def on_blinkStrengh_changed(self, blinkStrengh):
        self.time_difference = (datetime.now() - self.time)

        if self.task_step == 3:
            self.task_three(blinkStrengh)

        elif self.task_step == 4:
            self.task_four(blinkStrengh)

        elif self.task_step == 5:
            self.task_five(blinkStrengh, self.attention)

    def intro(self):
        if self.task_step == 0:
            self.write_message_from_database(ChatbotDatabase.welcome_messages)
            self.write_message_from_database(ChatbotDatabase.headband_instruction_messages)
            self.write_message_from_database(ChatbotDatabase.screen_explain_messages)
            self.task_step += 1

    def task_one(self, attention):
        if attention >= 80:
            self.write_message_from_database(ChatbotDatabase.task_successful_messages)
            self.write_message_from_database(ChatbotDatabase.second_task_messages)
            self.time = datetime.now()
            self.is_idle = False
            self.task_step += 1

        elif self.time_difference >= self.time_to_idle and self.is_idle is False:
            self.write_message_from_database(ChatbotDatabase.idle_messages)
            self.is_idle = True

        elif self.time_difference >= self.time_to_fail:
            self.write_message_from_database(ChatbotDatabase.task_failed_messages)
            self.write_message_from_database(ChatbotDatabase.second_task_messages)
            self.time = datetime.now()
            self.is_idle = False
            self.task_step += 1

    def task_two(self, meditation):
        if meditation >= 80:
            self.write_message_from_database(ChatbotDatabase.task_successful_messages)
            self.write_message_from_database(ChatbotDatabase.third_task_messages)
            self.time = datetime.now()
            self.is_idle = False
            self.task_step += 1

        elif self.time_difference >= self.time_to_idle and self.is_idle is False:
            self.write_message_from_database(ChatbotDatabase.idle_messages)
            self.is_idle = True

        elif self.time_difference >= self.time_to_fail:
            self.write_message_from_database(ChatbotDatabase.task_failed_messages)
            self.write_message_from_database(ChatbotDatabase.third_task_messages)
            self.time = datetime.now()
            self.is_idle = False
            self.task_step += 1

    def task_three(self, blinkStrengh):
        if blinkStrengh >= 100:
            self.write_message_from_database(ChatbotDatabase.task_successful_messages)
            self.write_message_from_database(ChatbotDatabase.fourth_task_messages)
            self.time = datetime.now()
            self.is_idle = False
            self.task_step += 1

        elif self.time_difference >= self.time_to_idle and self.is_idle is False:
            self.write_message_from_database(ChatbotDatabase.idle_messages)
            self.is_idle = True

        elif self.time_difference >= self.time_to_fail:
            self.write_message_from_database(ChatbotDatabase.task_failed_messages)
            self.write_message_from_database(ChatbotDatabase.fourth_task_messages)
            self.time = datetime.now()
            self.is_idle = False
            self.task_step += 1

    def task_four(self, blinkStrengh):
        if blinkStrengh >= 100:
            self.write_message_from_database(ChatbotDatabase.task_successful_messages)
            self.write_message_from_database(ChatbotDatabase.last_task_messages)
            self.time = datetime.now()
            self.is_idle = False
            self.task_step += 1

        elif self.time_difference >= self.time_to_idle and self.is_idle is False:
            self.write_message_from_database(ChatbotDatabase.idle_messages)
            self.is_idle = True

        elif self.time_difference >= self.time_to_fail:
            self.write_message_from_database(ChatbotDatabase.task_failed_messages)
            self.write_message_from_database(ChatbotDatabase.last_task_messages)
            self.time = datetime.now()
            self.is_idle = False
            self.task_step += 1

    def task_five(self, blinkStrengh, attention):
        if blinkStrengh >= 50 and attention >= 50:
            self.write_message_from_database(ChatbotDatabase.task_successful_messages)
            self.write_message_from_database(ChatbotDatabase.tutorial_end_messages)
            self.time = datetime.now()
            self.is_idle = False
            self.task_step = -1

        elif self.time_difference >= self.time_to_idle and self.is_idle is False:
            self.write_message_from_database(ChatbotDatabase.idle_messages)
            self.is_idle = True

        elif self.time_difference >= self.time_to_fail:
            self.write_message_from_database(ChatbotDatabase.task_failed_messages)
            self.write_message_from_database(ChatbotDatabase.tutorial_end_messages)
            self.time = datetime.now()
            self.is_idle = False
            self.task_step = -1
