class Metrics():

    @staticmethod
    def average(data: list) -> float:
        '''
        Calculates average for list of heart rate population numbers.
        Treat list as poplulation numbers.

        Parameters:
            data (list[int]): Heart rate population numbers.
        Returns:
            float: Average heart rate from heart rate data.
        '''
        sum = 0
        for num in data:
            sum += num
        return round(sum/len(data), 2)


    @staticmethod
    def maximum(data: list) -> float:
        '''
        Finds maximum heart rate from heart rate values.

        Parameters:
            data (list[int]): Heart rate population numbers.
        Returns:
            float: Maximum heart rate from heart rate data.
        '''
        max = float("-inf")
        for num in data:
            if num > max:
                max = num
        return max


    @staticmethod
    def variance(data: list) -> float:
        '''
        Calculates population variance from heart rate values.

        Parameters:
            data (list[int]): Heart rate population numbers.
        Returns:
            float: Population variance from heart rate data.
        '''
        mean = Metrics.average(data)
        numerator = 0
        for num in data:
            numerator += (num - mean)**2
        return round(numerator/len(data), 2)


    @staticmethod
    def standard_deviation(data: list) -> float:
        '''
        Calculates population standard deviation from heart rate values.

        Parameters:
            data (list[int]): Heart rate population numbers.
        Returns:
            float: Population standard deviation heart rate data.
        '''
        sigma = Metrics.variance(data)
        return round(sigma**0.5, 2)


    @staticmethod
    def print_results(stats: list[float]) -> None:
        '''
        Unpacks list of input summary statistics to print.

        Parameters:
            data (list[str]): List of summary statistics.
        '''
        max_num, avg, stdev = stats
        print(f"\nMaximum HR: {max_num} \nAverage HR: {avg:.2f} \nStandard Deviation HR: {stdev:.2f}")

   
    @staticmethod
    def brain(data: list) -> list[float]:
        '''
        Coordinates methods of class to return summary statistics from heart rate values.

        Parameters:
            data (list[int]): Heart rate population numbers.
        Returns:
            list[float]: Population heart rate max, average, and standard deviation.
        '''
        stats = []
        stats.append(Metrics.maximum(data))
        stats.append(Metrics.average(data))
        stats.append(Metrics.standard_deviation(data))
        return stats