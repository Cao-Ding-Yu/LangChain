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
本章介绍了如何在在线环境中初始化不同的大语言模型，包括 DeepSeek 和 OpenAI 的模型。

#### 学习案例：
- `01-deepseek-init-online.py` - 使用 DeepSeek 模型进行在线初始化
- `02-openai-init-online.py` - 使用 OpenAI 模型进行在线初始化
- `03-init_chat_model-init-online.py` - 初始化聊天模型

### 第二章：模型初始化（本地）
本章专注于如何在本地环境中使用 Ollama 运行本地大语言模型。

#### 学习案例：
- `01-deepseek_14b-ollama-local.py` - 使用 Ollama 初始化 DeepSeek 模型
- `02-deepseek_14b-ollama-invoke.py` - 通过 Ollama 调用模型
- `03-deepseek_14b-ollama-rich_print.py` - 结构化打印模型输出
- `04-deepseek_14b-stream-batch.py` - 流式和批量处理模型调用
- `05-deepseek_14b-async.py` - 异步模型调用
- `06-deepseek_14b-profile-params-config.py` - 模型参数动态配置
- `07-deepseek_14b-exception.py` - 异常处理

### 第三章：LangSmith
学习如何使用 LangSmith 进行模型的监控、调试和评估。

#### 学习案例：
- `01-deepseek_14b-LangSmith.py` - 使用 LangSmith 监控模型

### 第四章：提示模板（Prompt Template）
掌握提示模板的使用方法，提高模型输入的一致性和可维护性。

#### 学习案例：
- `01-deepseek_14b-message.py` - 消息列表的创建
- `02-deepseek_14b-messages.py` - 消息列表的裁剪
- `03-deepseek_14b-dialogue.py` - 基于消息列表的简易对话
- `04-qwen3.8_27b-content-blocks.py` - 多模态内容块
- `05-gpt-oss_20b-prompt.py` - 提示词模板的创建
- `06-gpt-oss_20b-template.py` - 提示词模板的使用
- `07-gpt-oss_20b-placeholder.py` - 占位符提示模板

### 第五章：工具（Tools）
学习如何为模型添加工具，使其能够执行特定任务。

#### 学习案例：
- `01-gpt-oss_20b-tool_init-with@tool.py` - 使用 @tool 装饰器定义工具
- `02-gpt-oss_20b-tool_init-without@tool.py` - 不使用装饰器的工具初始化
- `03-gpt-oss_20b-tool-messages.py` - 带有工具的消息交互
- `04-qwen3.8_27b-tools-messages.py` - 并行工具调用的消息交互

### 第六章：结构化输出
学习如何让模型输出结构化的数据格式，如 JSON、Pydantic 模型等。

#### 学习案例：
- `01-deepseek_14b-pydantic.py` - 使用 Pydantic 模型输出结构化数据
- `02-deepseek_14b-TypedDict.py` - 使用 TypedDict 输出结构化数据
- `03-deepseek_14b-JSON_Schema.py` - 使用 JSON Schema 输出结构化数据
- `04-deepseek_14b-@dataclass.py` - 使用 dataclass 输出结构化数据
- `05-deepseek_14b-JsonOutputParser.py` - 使用 JsonOutputParser 解析输出

### 第七章：代理（Agents）
学习如何构建智能代理，让模型能够自主执行任务。

#### 学习案例：
- `01-gpt-oss_20b-init-Agent.py` - 初始化 Agent
- `02-gpt-oss_20b-tool-Agent.py` - Agent 绑定 Tool
- `03-qwen3.8_27b-struct_output-Agent.py` - 结构化输出的 Agent
- `04-qwen3.8_27b-struct_output-handle_errors.py` - Agent 的错误处理
- `05-qwen3.8_27b-stream-Agent.py` - 流式响应的 Agent
- `06-qwen3.8_27b-Assistant.py` - 助手 Agent

### 第八章：中间件（Middleware）
学习如何使用中间件来增强模型的功能，如日志记录、错误处理、限流等。

#### 学习案例：
- `01-deepseek_14b-SummarizationMiddleware.py` - 摘要中间件
- `02-qwen3.8_27b-HumanInTheLoopMiddleware.py` - 人机协作中间件
- `03-gpt-oss_20b-PIIMiddleware.py` - 隐私信息保护中间件
- `04-gpt-oss_20b-TodoListMiddleware.py` - 待办事项中间件
- `05-gpt-oss_20b-ModelCallLimitMiddleware.py` - 模型调用限制中间件
- `06-gpt-oss_20b-ToolCallLimitMiddleware.py` - 工具调用限制中间件
- `07-gpt-oss_20b-ModelFallbackMiddleware.py` - 模型替换中间件
- `08-gpt-oss_20b-LLMToolSelectorMiddleware.py` - LLM 工具选择器中间件
- `09-gpt-oss_20b-ToolRetryMiddleware.py` - 工具重试中间件
- `10-gpt-oss_20b-ModelRetryMiddleware.py` - 模型重试中间件
- `11-gpt-oss_20b-LLMToolEmulator.py` - LLM 工具模拟器
- `12-gpt-oss_20b-ContextEditingMiddleware.py` - 上下文清理中间件
- `13-gpt-oss_20b-FilesystemFileSearchMiddleware.py` - 文件系统搜索中间件
- `14-gpt-oss_20b-Node-style-hooks-decorator.py` - Node 风格钩子装饰器
- `15-gpt-oss_20b-Node-style-hooks-class.py` - Node 风格钩子类
- `16-gpt-oss_20b-can_jump_to.py` - 跳转功能
- `17-gpt-oss_20b-wrap_model_call.py` - 模型调用钩子函数
- `18-gpt-oss_20b-wrap_tool_call.py` - 工具调用钩子函数
- `19-gpt-oss_20b-hooks.py` - 钩子机制

### 第九章：记忆（Memory）
学习如何实现模型的记忆功能，使模型能够记住之前的交互内容。

#### 学习案例：
- `01-gpt-oss_20b-InMemorySaver.py` - 内存存储器
- `02-gpt-oss_20b-SqliteSaver.py` - 数据库存储器
- `03-gpt-oss_20b-Delete.py` - 删除记忆
- `04-gpt-oss_20b-Cut.py` - 截断记忆
- `05-gpt-oss_20b-InMemory-Put-Get.py` - 内存存储的增删改查
- `06-gpt-oss_20b-DataBase-Put-Get.py` - 数据库存储的增删改查
- `07-gpt-oss_20b-Search.py` - 长期记忆的检索
- `08-gpt-oss_20b-Tool.py` - 基于 Tool 的长期记忆操作
- `09-gpt-oss_20b-Middleware.py` - 基于中间件的长期记忆操作

### 第十章：检索增强生成（RAG）
学习如何构建 RAG 系统，将模型与外部知识库结合。

#### 学习案例：
- `01-TextLoader.py` - 文本加载器
- `02-CSVLoader.py` - CSV 加载器
- `03-JSONLoader.py` - JSON 加载器
- `04-PyPDFLoader.py` - PDF 加载器
- `05-MinerU.py` - MinerU 加载器
- `06-UnstructuredWordDocumentLoader.py` - Word 文档加载器
- `07-UnstructuredMarkdownLoader.py` - Markdown 加载器
- `08-UnstructuredHTMLLoader.py` - HTML 加载器
- `09-DirectoryLoader.py` - 目录加载器
- `10-CharacterTextSplitter.py` - 字符文本分割器
- `11-RecursiveCharacterTextSplitter.py` - 递归字符文本分割器
- `12-TokenTextSplitter.py` - Token 文本分割器
- `13-SemanticChunker.py` - 语义分块器
- `14-HTMLHeaderTextSplitter.py` - HTML 头部标题分割器
- `15-CodeTextSplitter.py` - 代码文本分割器
- `16-MarkdownTextSplitter.py` - Markdown 文本分割器
- `17-embed.py` - 嵌入模型使用
- `18-Milvus-DDL.py` - Milvus 数据定义语言
- `19-Milvus-DML.py` - Milvus 数据操作语言
- `20-Milvus-DQL.py` - Milvus 数据查询语言
- `21-deepseek_14b-Assistant.py` - 结合 RAG 的助手

## 使用说明

每个文件都是独立的 Python 脚本，可以直接运行来查看对应的示例效果。建议按照章节顺序学习，从基础到高级逐步掌握 LangChain 的使用方法。

## 环境要求

- Python 3.8+
- LangChain 相关依赖包（已包含在 requirements.txt 中）

## 许可证

本项目仅供学习交流使用。