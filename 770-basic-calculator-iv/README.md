# 基本计算器 IV

## 描述

给定一个表达式 `expression` 如 `expression = "e + 8 - a + 5"` 和一个求值映射，如 `{"e": 1}`（给定的形式为 `evalvars = ["e"]` 和 `evalints = [1]`），返回表示简化表达式的标记列表，例如 `["-1*a","14"]`

  * 表达式交替使用块和符号，每个块和符号之间有一个空格。
  * 块要么是括号中的表达式，要么是变量，要么是非负整数。
  * 块是括号中的表达式，变量或非负整数。
  * 变量是一个由小写字母组成的字符串（不包括数字）。请注意，变量可以是多个字母，并注意变量从不具有像 `"2x"` 或 `"-x"` 这样的前导系数或一元运算符 。

表达式按通常顺序进行求值：先是括号，然后求乘法，再计算加法和减法。例如，`expression = "1 + 2 * 3"` 的答案是 `["7"]`。

输出格式如下：

  * 对于系数非零的每个自变量项，我们按字典排序的顺序将自变量写在一个项中。例如，我们永远不会写像 `"b*a*c"` 这样的项，只写 `"a*b*c"`。
  * 项的次数等于被乘的自变量的数目，并计算重复项。(例如，`"a*a*b*c"` 的次数为 4。)。我们先写出答案的最大次数项，用字典顺序打破关系，此时忽略词的前导系数。
  * 项的前导系数直接放在左边，用星号将它与变量分隔开(如果存在的话)。前导系数 1 仍然要打印出来。
  * 格式良好的一个示例答案是 `["-2*a*a*a", "3*a*a*b", "3*b*b", "4*a", "5*c", "-6"]` 。
  * 系数为 0 的项（包括常数项）不包括在内。例如，"0" 的表达式输出为 []。



**示例：**

    
    
    **输入：** expression = "e + 8 - a + 5", evalvars = ["e"], evalints = [1]
    **输出：** ["-1*a","14"]
    
    **输入：** expression = "e - 8 + temperature - pressure",
    evalvars = ["e", "temperature"], evalints = [1, 12]
    **输出：** ["-1*pressure","5"]
    
    **输入：** expression = "(e + 8) * (e - 8)", evalvars = [], evalints = []
    **输出：** ["1*e*e","-64"]
    
    **输入：** expression = "7 - 7", evalvars = [], evalints = []
    **输出：** []
    
    **输入：** expression = "a * b * c + b * a * c * 4", evalvars = [], evalints = []
    **输出：** ["5*a*b*c"]
    
    **输入：** expression = "((a - b) * (b - c) + (c - a)) * ((a - b) + (b - c) * (c - a))",
    evalvars = [], evalints = []
    **输出：** ["-1*a*a*b*b","2*a*a*b*c","-1*a*a*c*c","1*a*b*b*b","-1*a*b*b*c","-1*a*b*c*c","1*a*c*c*c","-1*b*b*b*c","2*b*b*c*c","-1*b*c*c*c","2*a*a*b","-2*a*a*c","-2*a*b*b","2*a*c*c","1*b*b*b","-1*b*b*c","1*b*c*c","-1*c*c*c","-1*a*a","1*a*b","1*a*c","-1*b*c"]
    



**提示：**

  1. `expression` 的长度在 `[1, 250]` 范围内。
  2. `evalvars, evalints` 在范围 `[0, 100]` 内，且长度相同。



# Basic Calculator IV

## Description



Given an `expression` such as `expression = "e + 8 - a + 5"` and an evaluation map such as `{"e": 1}` (given in terms of `evalvars = ["e"]` and `evalints = [1]`), return a list of tokens representing the simplified expression, such as `["-1*a","14"]`

  * An expression alternates chunks and symbols, with a space separating each chunk and symbol.
  * A chunk is either an expression in parentheses, a variable, or a non-negative integer.
  * A variable is a string of lowercase letters (not including digits.) Note that variables can be multiple letters, and note that variables never have a leading coefficient or unary operator like `"2x"` or `"-x"`.

Expressions are evaluated in the usual order: brackets first, then multiplication, then addition and subtraction. For example, `expression = "1 + 2 * 3"` has an answer of `["7"]`.

The format of the output is as follows:

  * For each term of free variables with non-zero coefficient, we write the free variables within a term in sorted order lexicographically. For example, we would never write a term like `"b*a*c"`, only `"a*b*c"`.
  * Terms have degree equal to the number of free variables being multiplied, counting multiplicity. (For example, `"a*a*b*c"` has degree 4.) We write the largest degree terms of our answer first, breaking ties by lexicographic order ignoring the leading coefficient of the term.
  * The leading coefficient of the term is placed directly to the left with an asterisk separating it from the variables (if they exist.)  A leading coefficient of 1 is still printed.
  * An example of a well formatted answer is `["-2*a*a*a", "3*a*a*b", "3*b*b", "4*a", "5*c", "-6"]` 
  * Terms (including constant terms) with coefficient 0 are not included.  For example, an expression of "0" has an output of [].

**Examples:**

    
    
    **Input:** expression = "e + 8 - a + 5", evalvars = ["e"], evalints = [1]
    **Output:** ["-1*a","14"]
    
    **Input:** expression = "e - 8 + temperature - pressure",
    evalvars = ["e", "temperature"], evalints = [1, 12]
    **Output:** ["-1*pressure","5"]
    
    **Input:** expression = "(e + 8) * (e - 8)", evalvars = [], evalints = []
    **Output:** ["1*e*e","-64"]
    
    **Input:** expression = "7 - 7", evalvars = [], evalints = []
    **Output:** []
    
    **Input:** expression = "a * b * c + b * a * c * 4", evalvars = [], evalints = []
    **Output:** ["5*a*b*c"]
    
    **Input:** expression = "((a - b) * (b - c) + (c - a)) * ((a - b) + (b - c) * (c - a))",
    evalvars = [], evalints = []
    **Output:** ["-1*a*a*b*b","2*a*a*b*c","-1*a*a*c*c","1*a*b*b*b","-1*a*b*b*c","-1*a*b*c*c","1*a*c*c*c","-1*b*b*b*c","2*b*b*c*c","-1*b*c*c*c","2*a*a*b","-2*a*a*c","-2*a*b*b","2*a*c*c","1*b*b*b","-1*b*b*c","1*b*c*c","-1*c*c*c","-1*a*a","1*a*b","1*a*c","-1*b*c"]
    

**Note:**

  1. `expression` will have length in range `[1, 250]`.
  2. `evalvars, evalints` will have equal lengths in range `[0, 100]`.


**Tags:** Stack, Hash Table, String

**Difficulty:** Hard

**思路:**
