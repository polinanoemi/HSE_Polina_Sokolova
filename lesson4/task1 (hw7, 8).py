"""
Реализуйте класс CourtCase.
При вызове метода конструктора экземпляра (__init__) должны создаваться следующие атрибуты экземпляра:
● case_number (строка с номером дела — обязательный параметр) передаётся в качестве аргумента при создании экземпляра
● case_participants (список по умолчанию пустой)
● listening_datetimes (список по умолчанию пустой)
● is_finished (значение по умолчанию False)
● verdict (строка по умолчанию пустая)

У экземпляра должны быть следующие методы:
● set_a_listening_datetime — добавляет в список listening_datetimes судебное
заседание (структуру можете придумать сами)
● add_participant — добавляет участника в список case_participants (можно просто ИНН)
● remove_participant — убирает участника из списка case_participants
● make_a_decision — вынести решение по делу, добавить verdict и сменить атрибут is_finished на True
"""
class CourtCase:
        def __init__(self, case_number):
            self.case_number = case_number
            self.case_participants = []
            self.listening_datetimes = []
            self.is_finished = False
            self.verdict = ""
            self.court_location = court_location
            self.case_status = case_status

        def set_a_listening_datetime(self, datetime):
            self.listening_datetimes.append(datetime)

        def add_participant(self, participant_id):
            self.case_participants.append(participant_id)

        def remove_participant(self, participant_id):
            if participant_id in self.case_participants:
                self.case_participants.remove(participant_id)

        def make_a_decision(self, verdict):
            self.verdict = verdict
            self.is_finished = True

        def case_status(self):
            status = "Case Number: {}\nCourt Location: {}\nParticipants: {}\nListening Datetimes: {}\nStatus: {}" \
                .format(self.case_number, self.court_location, len(self.case_participants),
                        len(self.listening_datetimes), "Finished" if self.is_finished else "Ongoing")
            if self.is_finished:
                status += "\nVerdict: {}".format(self.verdict)
            return status


"""
HW 8: Добавлен атрибут  court_location и case_status, добавлен метод case_status
"""