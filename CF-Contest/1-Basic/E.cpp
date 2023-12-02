#include <iostream>
#include <map>
#include <sstream>
#include <stack>
#include <unordered_map>
#include <vector>

class TrieNode
{
public:
    std::string data;
    std::unordered_map<std::string, TrieNode*> children;

    TrieNode(std::string str) :
        data{ std::move(str) }
    {}
};

class Trie
{
private:
    TrieNode* root = new TrieNode("");

public:
    Trie() = default;

    ~Trie()
    {
        free_trie(root);
    }

    void insert(const std::string& path)
    {
        auto components = split(path, '/');
        TrieNode* curr = root;

        for (const auto& component : components)
        {
            if (curr->children.find(component) == curr->children.end())
            {
                curr->children[component] = new TrieNode(component);
            }

            curr = curr->children[component];
        }
    }

    void print_tree()
    {
        std::stack<std::pair<TrieNode*, size_t>> nodes;
        nodes.push({root, 0});

        while (!nodes.empty())
        {
            auto [node, depth] = nodes.top();
            nodes.pop();

            for (size_t i = 1; i < depth; ++i)
            {
                std::cout << "  ";
            }

            if (!node->data.empty())
            {
                std::cout << node->data << std::endl;
            }

            const auto as_map = std::map(node->children.cbegin(), node->children.cend());

            for (auto it = as_map.rbegin(); it != as_map.rend(); ++it)
            {
                nodes.push({it->second, depth + 1});
            }
        }
    }

private:
    std::vector<std::string> split(const std::string& s, const char delimiter)
    {
        std::vector<std::string> tokens;
        std::string token;
        std::istringstream stream(s);

        while (std::getline(stream, token, delimiter))
        {
            tokens.emplace_back(std::move(token));
        }

        return tokens;
    }

    void free_trie(TrieNode* root)
    {
        std::stack<TrieNode*> nodes;
        nodes.push(root);

        while (!nodes.empty())
        {
            auto node = nodes.top();
            nodes.pop();

            for (const auto& pair : node->children)
            {
                nodes.push(pair.second);
            }

            delete node;
        }
    }
};

int main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);

    size_t N;
    std::cin >> N;
    std::cin.ignore();

    std::vector<std::string> paths;
    for (size_t i = 0; i < N; ++i)
    {
        std::string path;
        std::getline(std::cin, path);
        paths.emplace_back(std::move(path));
    }

    Trie trie;
    for (const auto& path : paths)
    {
        trie.insert(path);
    }

    trie.print_tree();
    return 0;
}
