#　筛选出需要的网页内容
import re


html1 = """
<p>晋升空间大 架构健全</p>
    </dd>
    <dd class="job_bt">
        <h3 class="description">职位描述：</h3>
        <div class="job-detail">
        <p>岗位职责：</p>
<p>1、参与基础架构设计、核心模块开发、调试与维护工作；<br>2、负责业务功能的设计、研发与维护；<br>3、参与公司技术架构优化改进、升级迭代；<br>4、协助并完成其他各类技术开发任务。</p>
<p>任职要求：</p>
<p>计算机及相关专业，大学本科及以上学历；<br>至少3年JAVA开发经验，熟悉Java Heap、Stack、多线程等相关概念；<br>有微服务框架的设计与开发经验;<br>熟悉JPA、MyBatis或Hibernate等ORM框架；<br>有MySQL开发经验，有Redis使用经验；<br>具有良好的沟通能力及团队意识、工作认真负责、踏实肯干、积极主动。</p>
<p>加分项：<br>熟悉Scala语言并有相关项目开发经验；<br>有JMS MQ，Rabbit MQ或者Kafka等消息系统使用经验；<br>熟悉Cassandra、MongoDB、HBase等NoSQL数据库系统。</p>
<p></p>

"""

# [^>]表示只要不是>就可以，　r"<[^>]>"表示<>里只有一个字符的标签才会被替换
ret = re.sub(r"<[^>]>", "", html1)
print(ret)

# [^>]表示只要不是>就可以，　r"<[^>]*>"表示<>里有任意标签就会会被替换
ret = re.sub(r"<[^>]*>", "", html1)
print(ret)