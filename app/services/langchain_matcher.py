import logging
from typing import List

from langchain_core.messages import HumanMessage, SystemMessage

logger = logging.getLogger(__name__)


def match_string_with_langchain(input_string: str, list_of_strings: List[str], model) -> str:
    """
    Matches an input string to one of a list of strings using a LangChain model.

    Args:
        input_string: The string to match.
        list_of_strings: A list of strings to match against.
        model: The LangChain model object (e.g., a ChatOpenAI instance).

    Returns:
        The model's response content.
    """
    system_prompt = f"""
    Match the input string to one of these : {list_of_strings}. If you can't find a match, return 'None'.
    """

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=input_string),
    ]

    logger.info("Using LLM to find match for %s", input_string)
    response = model.invoke(messages)

    content = getattr(response, "content", "")
    logger.info("Response = %s", content)
    return content


