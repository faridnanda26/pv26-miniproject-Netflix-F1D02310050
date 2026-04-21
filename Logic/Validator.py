class Validator:
    
    @staticmethod
    def title_validation(title):
        if not title:
            return False, "The movie title cannot be left blank" # hanya cek field title tidak boleh kosong
        return True, ""