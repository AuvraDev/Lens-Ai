class FileHandler:
    """
    A class to handle file operations.
    """

    @staticmethod
    def read_file(file_path):
        """
        Reads the contents of a file and returns it.
        :param file_path: The path to the file.
        :return: The content of the file.
        """
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return None

    @staticmethod
    def write_file(file_path, content):
        """
        Writes content to a file.
        :param file_path: The path to the file.
        :param content: The content to write.
        """
        with open(file_path, 'w') as file:
            file.write(content)


class DateTimeHelper:
    """
    A class to help with date and time operations.
    """

    @staticmethod
    def get_current_utc():
        """
        Returns the current date and time in UTC.
        :return: The current UTC datetime in ISO format.
        """
        from datetime import datetime
        return datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')


class ResponseHelper:
    """
    A class for standardized API responses.
    """

    @staticmethod
    def success(data, message='Request was successful.'): 
        """
        Returns a successful API response.
        :param data: The data to return.
        :param message: The success message.
        :return: A dictionary representing the response.
        """
        return {'status': 'success', 'message': message, 'data': data}

    @staticmethod
    def error(message, status_code=400):
        """
        Returns an error API response.
        :param message: The error message.
        :param status_code: The HTTP status code.
        :return: A dictionary representing the response.
        """
        return {'status': 'error', 'message': message, 'status_code': status_code}
