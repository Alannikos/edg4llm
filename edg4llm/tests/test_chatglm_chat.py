from edg4llm.models.chatglm import EDGChatGLM

if __name__ == "__main__":
    # 替换为你的实际 API 密钥
    api_key = "479dc4c9611acd56f0b7981f126a3411.tNS782K8hcuk1UeO"
    base_url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"
    chat_glm = EDGChatGLM(base_url=base_url, api_key=api_key)

    try:
        system_prompt = "你叫作Alannikos"
        user_prompt = "你是谁"
        response = chat_glm.execute_request(system_prompt=system_prompt, user_prompt=user_prompt, model='glm-4-flash')
        print(f"输出: {response}")
    except Exception as e:
        # print(f"调用失败，错误信息: {e}")
        exit()
