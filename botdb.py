import sqlite3


class BotDB:
    
    def __init__(self, db_file):
        self.conn= sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def check_user(self, user_id):
        result = self.cursor.execute(f"SELECT * FROM `users` WHERE `user_telegram_id` = (?) ", (str(user_id),))
        return result.fetchall()
    
    def add_user(self,user_id):
        self.cursor.execute("INSERT INTO `users` (`user_telegram_id`) VALUES (?)", (str(user_id),))
        print('Новый пользователь внесен в базу данных')
        return self.conn.commit()
        
    def add_note(self, user_id, text):
        self.cursor.execute("INSERT INTO `notes` (`user_telegram_id`,`note`) VALUES (?,?) ",(str(user_id), text))
        return self.conn.commit()

    def show_notes(self, user_id):
        result = self.cursor.execute("SELECT `note` FROM `notes` WHERE `user_telegram_id` = (?)", (str(user_id),))
        return result.fetchall()

    def del_notes(self, user_id):
        result = self.cursor.execute("DELETE FROM `notes` WHERE `user_telegram_id` = (?)", (str(user_id),))
        return self.conn.commit()

    def check_notes(self, user_id):
        result = self.cursor.execute("SELECT `note` FROM `notes` WHERE `user_telegram_id` = (?)", (str(user_id),))
        return bool(len(result.fetchall()))



    def show_notes(self, user_id,rang):
        print('------запускаю')
        if rang == 24:
            print('------за день')
            result = self.cursor.execute("SELECT `note` FROM `notes` WHERE `user_telegram_id` = (?) AND `date` BETWEEN datetime('now', 'start of day') AND datetime('now', 'localtime')  ORDER BY `date` ", (str(user_id),))
        if rang == 7:
            result = self.cursor.execute("SELECT `note` FROM `notes` WHERE `user_telegram_id` = (?) AND `date` BETWEEN datetime('now', '-6 days') AND datetime('now', 'localtime') ORDER BY `date` ", (str(user_id),))
        if rang == 31:
            result = self.cursor.execute("SELECT `note` FROM `notes` WHERE `user_telegram_id` = (?) AND `date` BETWEEN datetime('now', 'start of month') AND datetime('now', 'localtime') ORDER BY `date`", (str(user_id),))
        if rang == 0:
            result = self.cursor.execute("SELECT `note` FROM `notes` WHERE `user_telegram_id` = (?) ", (str(user_id),))
        
        return result.fetchall()
        
