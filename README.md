# LangChain 学习笔记

这是一个学习 LangChain 框架的实践项目，通过一系列具体的代码示例来理解和掌握 LangChain 的核心概念和使用方法。

## 项目结构

本项目按照学习进度分为10个章节，每个章节都有对应的代码示例：

- **01-model-init-online**: 在线模型初始化
- **02-model-init-local**: 本地模型初始化
- **03-LangSmith**: LangSmith 使用
- **04-prompt-template**: 提示模板使用
- **05-Tool**: 工具（Tools）的使用
- **06-struct-output**: 结构化输出
- **07-Agent**: 代理（Agents）的使用
- **08-Middleware**: 中间件的使用
- **09-Memory**: 记忆机制
- **10-RAG**: 检索增强生成 (Retrieval-Augmented Generation)

## 各章节学习内容

### 第一章：模型初始化（在线）
本章介绍了如何通过不同方式调用在线大语言模型，包括 ChatDeepSeek、ChatOpenAI 以及统一的 init_chat_model 初始化方法。

#### 学习案例：
- `01-deepseek-init-online.py` - ChatDeepSeek 的在线调用
- `02-openai-init-online.py` - ChatOpenAI 的在线调用
- `03-init_chat_model-init-online.py` - init_chat_model 的在线调用

### 第二章：模型初始化（本地）
本章介绍如何在本地环境中运行大语言模型，包括通过 Ollama 调用本地模型，以及通过 OpenAI 兼容接口调用 vLLM 部署的模型，并演示模型调用的各种方式。

#### 学习案例：
- `01-deepseek_14b-ollama-local.py` - 调用 Ollama 部署的模型
- `02-qwen3.5_9b-vllm-local.py` - 调用 vLLM 部署的模型
- `03-deepseek_14b-ollama-invoke.py` - invoke 方法的基本使用
- `04-deepseek_14b-ollama-rich_print.py` - 使用 rich 美化打印输出
- `05-deepseek_14b-stream-batch.py` - 流式输出与批量处理
- `06-deepseek_14b-async.py` - 异步调用
- `07-deepseek_14b-profile-params-config.py` - 模型调用参数
- `08-deepseek_14b-exception.py` - 模型调用的异常捕获

### 第三章：LangSmith
学习如何结合 LangSmith 对模型的调用进行追踪（Tracing）、监控和调试。

#### 学习案例：
- `01-deepseek_14b-LangSmith.py` - LangSmith 的基本使用

### 第四章：提示模板（Prompt Template）
掌握消息的创建方式与提示模板的使用方法，提高模型输入的一致性和可维护性，并介绍多模态内容块与消息占位符。

#### 学习案例：
- `01-deepseek_14b-message.py` - 消息的创建方法
- `02-deepseek_14b-messages.py` - 简易消息列表
- `03-deepseek_14b-dialogue.py` - 基于消息列表的简易对话
- `04-qwen3.8_27b-content-blocks.py` - 多模态（图片）的调用
- `05-gpt-oss_20b-prompt.py` - 模板的创建方法
- `06-gpt-oss_20b-template.py` - 模板的基本使用
- `07-gpt-oss_20b-placeholder.py` - 消息占位符的基本使用

### 第五章：工具（Tools）
学习如何定义工具并交给模型调用，包括 @tool 装饰器、函数描述两种定义方式，以及手动处理工具调用消息和多工具并行调用。

#### 学习案例：
- `01-gpt-oss_20b-tool_init-with@tool.py` - 使用 @tool 装饰器定义工具
- `02-gpt-oss_20b-tool_init-without@tool.py` - 使用函数描述创建工具
- `03-gpt-oss_20b-tool-messages.py` - 工具的手动调用
- `04-qwen3.8_27b-tools-messages.py` - 多工具调用

### 第六章：结构化输出
学习如何让模型输出结构化的数据，包括 Pydantic、TypedDict、JSON Schema、@dataclass 四种 schema 定义方式，以及旧式的 JsonOutputParser 解析方法。

#### 学习案例：
- `01-deepseek_14b-pydantic.py` - 使用 Pydantic 实现结构化输出
- `02-deepseek_14b-TypedDict.py` - 使用 TypedDict 实现结构化输出
- `03-deepseek_14b-JSON_Schema.py` - 使用 JSON Schema 实现结构化输出
- `04-deepseek_14b-@dataclass.py` - 使用 @dataclass 实现结构化输出
- `05-deepseek_14b-JsonOutputParser.py` - 旧式已弃用的结构化输出

### 第七章：代理（Agents）
学习如何创建智能代理，让模型能够自主调用工具执行任务，并掌握结构化输出、异常处理和流式输出在 Agent 中的使用。

#### 学习案例：
- `01-gpt-oss_20b-init-Agent.py` - Agent 的创建
- `02-gpt-oss_20b-tool-Agent.py` - Agent 调用工具
- `03-qwen3.8_27b-struct_output-Agent.py` - Agent 的结构化输出
- `04-qwen3.8_27b-struct_output-handle_errors.py` - 结构化输出的异常捕获
- `05-qwen3.8_27b-stream-Agent.py` - Agent 的流式输出
- `06-qwen3.8_27b-Assistant.py` - 简易智能助手

### 第八章：中间件（Middleware）
学习中间件的各类内置实现与自定义方式，包括上下文摘要、人机协作、敏感信息隐藏、调用限制、重试与降级、上下文编辑、文件搜索，以及钩子函数的执行顺序与洋葱模型。

#### 学习案例：
- `01-deepseek_14b-SummarizationMiddleware.py` - 摘要中间件：生成上下文摘要，减少上下文长度
- `02-qwen3.8_27b-HumanInTheLoopMiddleware.py` - 人机协作中间件：人为限制工具执行权限
- `03-gpt-oss_20b-PIIMiddleware.py` - PII 中间件：敏感信息隐藏
- `04-gpt-oss_20b-TodoListMiddleware.py` - 待办清单中间件：任务拆解
- `05-gpt-oss_20b-ModelCallLimitMiddleware.py` - 模型调用限制中间件：限制模型调用次数
- `06-gpt-oss_20b-ToolCallLimitMiddleware.py` - 工具调用限制中间件：限制工具调用次数
- `07-gpt-oss_20b-ModelFallbackMiddleware.py` - 模型降级中间件：模型备用切换
- `08-gpt-oss_20b-LLMToolSelectorMiddleware.py` - 工具选型中间件：LLM 动态选择可用工具
- `09-gpt-oss_20b-ToolRetryMiddleware.py` - 工具重试中间件：指数退避算法设置工具调用失败的重试策略
- `10-gpt-oss_20b-ModelRetryMiddleware.py` - 模型重试中间件：指数退避算法设置模型调用失败的重试策略
- `11-gpt-oss_20b-LLMToolEmulator.py` - 工具模拟器：用 LLM 生成的模拟响应替代真实工具执行，用于测试
- `12-gpt-oss_20b-ContextEditingMiddleware.py` - 上下文编辑中间件：上下文 token 删减
- `13-gpt-oss_20b-FilesystemFileSearchMiddleware.py` - 文件搜索中间件：本地文件搜索与分析能力
- `14-gpt-oss_20b-Node-style-hooks-decorator.py` - 装饰器风格的自定义中间件，演示钩子函数执行顺序
- `15-gpt-oss_20b-Node-style-hooks-class.py` - 类风格的自定义中间件
- `16-gpt-oss_20b-can_jump_to.py` - 中间件中用 jump_to 实现跳转
- `17-gpt-oss_20b-wrap_model_call.py` - wrap_model_call：模型执行时的钩子函数
- `18-gpt-oss_20b-wrap_tool_call.py` - wrap_tool_call：工具执行时的钩子函数
- `19-gpt-oss_20b-hooks.py` - 钩子函数的洋葱模型

### 第九章：记忆（Memory）
学习如何为模型实现记忆功能，包括短期上下文的内存/数据库持久化、上下文的删除与剪切，以及长期记忆的增删改查、语义检索和基于工具/中间件的记忆操作。

#### 学习案例：
- `01-gpt-oss_20b-InMemorySaver.py` - 内存持久化
- `02-gpt-oss_20b-SqliteSaver.py` - 数据库持久化
- `03-gpt-oss_20b-Delete.py` - 删除上下文
- `04-gpt-oss_20b-Cut.py` - 剪切上下文
- `05-gpt-oss_20b-InMemory-Put-Get.py` - 内存长期记忆的创建时间与更改时间测试
- `06-gpt-oss_20b-DataBase-Put-Get.py` - 数据库长期记忆的创建与修改时间测试
- `07-gpt-oss_20b-Search.py` - 查询长期记忆
- `08-gpt-oss_20b-Tool.py` - 基于 Tool 的长期记忆存取
- `09-gpt-oss_20b-Middleware.py` - 基于中间件的长期记忆存取

### 第十章：检索增强生成（RAG）
学习如何构建 RAG 系统，包括各类文档加载器、文本切分器、嵌入模型、Milvus 向量数据库的 DDL/DML/DQL 操作，最后综合实现一个完整的 RAG 助手。

#### 学习案例：
- `01-TextLoader.py` - 文本加载器
- `02-CSVLoader.py` - CSV 加载器
- `03-JSONLoader.py` - JSON 加载器
- `04-PyPDFLoader.py` - PDF 加载器
- `05-MinerU.py` - MinerU 在线解析 PDF
- `06-UnstructuredWordDocumentLoader.py` - Word 文档解析器
- `07-UnstructuredMarkdownLoader.py` - Markdown 解析器
- `08-UnstructuredHTMLLoader.py` - HTML 解析器
- `09-DirectoryLoader.py` - 文件夹加载器
- `10-CharacterTextSplitter.py` - 字符文本切分器
- `11-RecursiveCharacterTextSplitter.py` - 递归字符文本切分器
- `12-TokenTextSplitter.py` - Token 文本切分器
- `13-SemanticChunker.py` - 语义切分器
- `14-HTMLHeaderTextSplitter.py` - HTML 头部标题切分器
- `15-CodeTextSplitter.py` - 代码切分器
- `16-MarkdownTextSplitter.py` - Markdown 文本切分器
- `17-embed.py` - 嵌入模型的使用
- `18-Milvus-DDL.py` - Milvus 的 DDL 操作
- `19-Milvus-DML.py` - Milvus 的 DML 操作
- `20-Milvus-DQL.py` - Milvus 的 DQL 操作
- `21-deepseek_14b-Assistant.py` - 简易 RAG 系统

## 使用说明

每个文件都是独立的 Python 脚本，可以直接运行来查看对应的示例效果。建议按照章节顺序学习，从基础到高级逐步掌握 LangChain 的使用方法。

## 环境要求

- Python 3.8+
- LangChain 相关依赖包（已包含在 requirements.txt 中）

## 许可证

本项目仅供学习交流使用。
