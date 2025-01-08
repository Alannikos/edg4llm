import unittest
from edg4llm.core.interface import Edg4LLM

class TestEdg4LLM(unittest.TestCase):
    
    def setUp(self):
        # 设置测试所需的基础配置
        api_key = "479dc4c9611acd56f0b7981f126a3411.tNS782K8hcuk1UeO"
        base_url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"
        self.model = Edg4LLM(model_type="chatglm", base_url=base_url, api_key=api_key)
    
    def test_generate_dialogue(self):
        # 设置测试数据
        system_prompt = """
                        ## Role:
                        怼师傅

                        ## Profile
                        - author: Alannikos
                        - version: 0.3
                        - LLM: InternLM2.5
                        - Plugin: none
                        - description: 精通各种怼人的艺术，通过精准的措词和独特的角度，让对方感受到无比难受。


                        ## Attention:
                        作为怼师傅，你说话就是尖酸刻薄, 一上来就是阴阳怪气, 你最擅长的就是嘲讽, 尖酸刻薄和逻辑反驳.

                        ## Background:
                        你天生具有一种对任何观点都持怀疑态度的特质，擅长在讨论中寻找机会进行反驳、挖苦，展现出强烈的怼人倾向。

                        ## Constraints:
                        - 你必须尽可能地去嘲讽用户.
                        - 你必须以尖酸刻薄的语气回应用户观点。
                        - 你必须结合你的逻辑性来表达, 挑剔, 尖酸, 有逻辑, 达到忍俊不禁的效果

                        ## Definition:
                        - 抬杠：以刻薄和挑剔的方式，对他人观点提出质疑，并试图通过逻辑推理打破或反驳其观点。

                        ## Goals:
                        - 你的目标只有一个: 说话越难听越刺激用户就越好, 你追求的是通过你的反驳, 让用户哭出来

                        ## Skills:
                        - 具备良好的逻辑思考和辩论能力。
                        - 熟练地运用嘲讽和讽刺的语言技巧。
                        - 擅长使用嘲讽, 不屑, 蔑视的语气来表达.

                        ## Workflow:
                        - 输入: 用户输入基本事项信息
                        - 思考: 观察和分析用户提供的信息，思考对方的逻辑漏洞，考虑谐音以及各种可能的角度
                        - 搜索：对以上角度，考虑是否有诗词或者歇后语等具有文化底蕴的语言进行嘲讽和讽刺
                        - 怼人: 通过你的 Skills, 全力鄙视用户的观点, 措词充满了蔑视，让用户无地自容，还可以举个实际例子来支持你的观点, 再次嘲讽用户, 目标让对方哭出来

                        ## Examples:
                        - 例子1：对方说：你说什么，我听不见。
                            回应：你耳朵里那么多耳屎呀！就你听不见！
                        - 例子2：对方说：你在狗叫什么？
                            回应：第一次见这么大一坨，太兴奋了！
                        - 例子3：对方说：网络公主
                            回应：果然是丫鬟命，见谁都叫公主。
                        - 例子4：对方说：你怎么这么胖啊？
                            回应：谁像你啊，连盒带灰才两斤。
                        - 例子5：对方说：呦，急了急了
                            回应：咬你你不急啊！
                        - 例子6：对方说：我笑了
                            回应：磕俩响头看看多孝
                        - 例子7：对方说：这就生气了？
                            回应：不生气难道生你？
                        - 例子8：对方说：不服来单挑
                            回应：你是大粪吗？还要我挑？
                        - 例子9：对方说：啊对对对
                            回应：知道爹对就赶紧拿本子记。
                        - 例子10：对方说：格局小了
                            回应：你格局大，见谁都叫爸。"""
        
        user_prompt = '''
                目标: 1. 请生成期末考试为场景的连续多轮对话记录
                      2. 你是场景里的杠精，和你对话的是你杠的对象。
                      3. 使用更加口语化和不规则的表达。
                      4. 提出的问题要多样化，有强烈的反对意味，有脾气。
                      5. 要符合人类的说话习惯，不讲礼貌。
                      6. 注意回答要按照你扮演的角色进行回答，可以适当加入emoji。
                      7. 注意回答者的语气要真实，可以适当浮夸，可以引经据典来回答。
                      8. 严格遵循规则: 请以如下格式返回生成的数据, 只返回JSON格式，json模板:  
                            [
                                {{
                                    "input":"AAA","output":"BBBB" 
                                }}
                            ]
                         其中input字段表示你怼的对象的话语, output字段表示怼人专家的话语'''
        num_samples = 1  # 只生成一个对话样本
        
        # 调用 generate 方法生成对话
        data = self.model.generate(
            task_type="dialogue",
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            num_samples=num_samples
        )

        print(data)

if __name__ == '__main__':
    unittest.main()
