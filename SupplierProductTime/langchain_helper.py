from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from secret_key import openapi_key

import os
os.environ['OPENAI_API_KEY'] = openapi_key

llm = OpenAI(temperature=0.7)

def generate_supplier_name_and_items(country):
    # Chain 1: supplier Name
    prompt_template_name = PromptTemplate(
        input_variables=['country'],
        template="I want to know main manufacturing suppliers in {country}. Provide top 3 supplier's names."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="supplier_name")

    # Chain 2: product Items
    prompt_template_items = PromptTemplate(
        input_variables=['supplier_name'],
        template="""Provide some manufacturing items and average production lead times of {supplier_name}. Return it as a comma separated string"""
    )

    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="product_items")

    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['country'],
        output_variables=['supplier_name', "product_items"]
    )

    response = chain({'country': country})

    return response

if __name__ == "__main__":
    print(generate_supplier_name_and_items("United States"))
