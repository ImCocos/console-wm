from typing import List


class Content:
    def __init__(self, text: str | List[str] | List[List[str]]) -> None:
        self.text_array = self.arraify(text)
    
    def arraify(self, text: str | List[str] | List[List[str]]) -> List[List[str]]:
        if isinstance(text, str):
            return [
                [
                    let for let in string
                ] for string in text.strip().split('\n')
            ]
        if isinstance(text[0], list):
            return text # type: ignore

        return [
            [
                let for let in string
            ] for string in text
        ]
            