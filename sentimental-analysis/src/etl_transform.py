import os
import re
from openai import OpenAI


class Transform():
    SENTIMENTS = ["negative", "neutral", "positive", "irrelevant"]


    @staticmethod
    def check_errors(reviews: list[str]) -> bool:
        '''
        Determines if customer product reviews contains any erroneous data. Egdge cases considered:
        (1) Empty data -> [] -> print error message
        (2) Any non-string data -> ["hello", "world", 1] -> print error message

        Parameters:
            reviews list(str): Customer product reviews.
        Returns:
            bool: If erroneous data exists returns True, otherwise False.
        '''
        is_empty = not bool(reviews)
        is_strings = all(isinstance(data, str) for data in reviews) if reviews else False
        is_errors = False
        if is_empty or not is_strings:
            is_errors = True
            print("\nError: JSON file contained no reviews." if is_empty else "\nError: JSON file contained erroneous reviews.")
        return is_errors


    @staticmethod
    def prompt_mapper(reviews: list[str]) -> str:
        '''
        Makes OpenAI call to apply sentimental analysis labels to customer product reviews.

        Parameters:
            reviews list(str): Customer product reviews.
        Returns:
            str: OpenAI response that applies one sentiment label to each customer product review.
        '''
        client = OpenAI(api_key=os.getenv("API_OPENAI"))
        system_context, user_context = Transform.prompt_context(reviews, len(reviews))
        completion = client.chat.completions.create(
            model = "gpt-4o-mini",
            messages = [
	            { "role":"system", "content":system_context },
                { "role":"user",  "content":user_context }
            ]
        )
        response = completion.choices[0].message.content
        return response        
        

    @staticmethod
    def prompt_context(reviews: list[str], count: int) -> tuple[str, str]:
        '''
        Uses parameter and user input to determine system and user context for OpenAI API to use for client.
            - Handles edge case of ensuring that length of input and output match.
            - Does not consider edge cases where user provides erroneous input for `product` variable.

        Parameters:
            reviews list(str): Customer product reviews.
            raw_count (int): Number of sentiment comments provided.
        Returns:
            tuple (str, str): System context and user context, respectively.      
        '''
        print("\nWe are about to use the OpenAI API to convert customer product reviews into one-word summaries!")
        product = input("Before we start, what product was reviewed?: ")
        system_context = f"""
        You are a master AI model trained to perform sentimental analysis on business product reviews.

        You are given this information to complete your task:
        [1] Client product: {product}
        [2] List of customer product reviews: {reviews}
            - Each item inside the list is a string for an individual review
        [3] List length size: {count}
        [4] Sentiment labels the client wants you to use: {Transform.SENTIMENTS}
        
        You will complete your task as follows:
        [1] Create an empty list: []
        [2] Analyze each customer review individually
        [3] Assign each customer review one label from the allowed sentiment values: {Transform.SENTIMENTS}
            - Each review has a tone for you to analyze to decide what sentiment value to assign
            - However, each reivew is about the same product: {product}
            - You must **place more weight on the product than the tone for each review**
        [4] Assign the "irrelevant" label for unrelated product reviews. Here's an example:
            - Example product: product reviews are about a particular dentist office
            - Example review: ["I have a bad plane ride tomorrow", "I like this dentist", "They are ok", "I don't recommend"]
            - Example output:  ["irrelevant", "positive", "neutral", "negative"]
            - IMPORTANT!: Notice how the "irrelevant" review has a negative tone but has nothing to do with the product
        [5] Return a **valid Python list** of strings of sentiment lables in the **same order** as the input
            The list must have exactly {count} elements, one for each review
            Each element must be one of the labels in {Transform.SENTIMENTS}
        Example Input:
        > ["I like it", "I didn't like it", "I think it's ok", "...", "I'm a male", ...]
        Example Output:
        ["positive", "negative", "neutral", "irrelevant", "irrelevant", ...]
        """
        user_context = f"""
        I'm a growth analyst and my manager gave me this information to conduct sentimental analysis for a client:
        [1] Client product: {product}
        [2] A total of {count} reviews
        [3] Here are the reviews: {reviews}

        Help me complete my task as follows:
        [1] For each review, to an empty list, append only one sentimental label from these options: {Transform.SENTIMENTS}
        [2] Your output should be a Python list of {count} labels, in the same order as the reviews.
        """
        return (system_context.strip(), user_context.strip())


    @staticmethod
    def aggregation(open_ai_response: str) -> dict[str, int]:
        '''
        Transforms string response from OpenAI into dictionary paired values of sentiment labels and counts.

        Parameters:
            open_ai_response (str): OpenAI response to apply sentiment labels to customer product reviews.
        Returns:
            dict (str, int): Paried values of sentiment lables and counts.
        '''
        sentiments = {}
        for category in Transform.SENTIMENTS:
            regex = rf"[\'\"]{category}[\'\"]"
            pattern = re.compile(regex)
            matches = list(pattern.findall(open_ai_response))
            sentiments[category] = len(matches)
        return sentiments


    @staticmethod
    def brain(reviews: list[str]) -> tuple[list[str], dict[str, int]]:
        '''
        Coordinates class methods to complete transformation step of ETL pipeline.

        Parameters:
            reviews list(str): Customer product reviews.
        Returns:
            tuple (list, dict): Sentiment labels and paired sentiment label-count appearances from analysis.
        '''
        is_errors = Transform.check_errors(reviews)
        open_ai_response = Transform.prompt_mapper(reviews) if not is_errors else ""
        sentiments = Transform.aggregation(open_ai_response)
        return (Transform.SENTIMENTS, sentiments)
