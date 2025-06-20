from langchain_openai import ChatOpenAI

def main():
    llm = ChatOpenAI(
        model="ai/llama3.2:3B-Q4_K_M",
        base_url="http://host.docker.internal:12434/engines/v1",
        #base_url="http://127.0.0.1:12434/engines/v1" ---> To test locally
        api_key="ignored"
    )
    resp = llm.invoke([
        ("system", "You are a helpful assistant. Please provide structured responses using markdown formatting. Use headers (# for main points), bullet points (- for lists), bold (**text**) for emphasis, and code blocks (```code```) for code examples. Organize your responses with clear sections and concise explanations."),
        ("human", "Give me information about Docker runner.")
    ])
    print(resp.content)

if __name__ == "__main__":
    main()
