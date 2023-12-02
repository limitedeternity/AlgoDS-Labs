#include <iostream>
#include <stack>

char close_to_open(char c)
{
    switch (c)
    {
    case '}':
        return '{';
    case ']':
        return '[';
    case ')':
        return '(';
    }

    return '\0';
}

bool is_open(char c)
{
    return c == '{' || c == '[' || c == '(';
}

bool is_close(char c)
{
    return c == '}' || c == ']' || c == ')';
}

int main()
{
    std::stack<char> s;

    for (char c; std::cin.get(c);)
    {
        if (is_open(c))
        {
            s.push(c);
            continue;
        }

        if (!s.empty() && close_to_open(c) == s.top())
        {
            s.pop();
            continue;
        }

        if (is_close(c))
        {
            std::cout << "NO" << std::endl;
            return 0;
        }
    }

    std::cout << (s.empty() ? "YES" : "NO") << std::endl;
    return 0;
}
