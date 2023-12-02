#include <iostream>
#include <vector>

size_t _mergeSort(unsigned long long arr[], unsigned long long temp[], size_t left, size_t right);
size_t merge(unsigned long long arr[], unsigned long long temp[], size_t left, size_t mid, size_t right);

size_t mergeSort(unsigned long long arr[], size_t array_size)
{
    unsigned long long temp[array_size];
    return _mergeSort(arr, temp, 0, array_size - 1);
}

size_t _mergeSort(unsigned long long arr[], unsigned long long temp[], size_t left, size_t right)
{
    size_t mid, inv_count = 0;

    if (right > left)
    {
        mid = (right + left) / 2;

        inv_count += _mergeSort(arr, temp, left, mid);
        inv_count += _mergeSort(arr, temp, mid + 1, right);
        inv_count += merge(arr, temp, left, mid + 1, right);
    }

    return inv_count;
}

size_t merge(unsigned long long arr[], unsigned long long temp[], size_t left, size_t mid, size_t right)
{
    size_t i, j, k;
    size_t inv_count = 0;

    i = left;
    j = mid;
    k = left;

    while (i <= mid - 1 && j <= right)
    {
        if (arr[i] <= arr[j])
        {
            temp[k++] = arr[i++];
        }
        else
        {
            temp[k++] = arr[j++];
            inv_count = inv_count + (mid - i);
        }
    }

    while (i <= mid - 1)
    {
        temp[k++] = arr[i++];
    }

    while (j <= right)
    {
        temp[k++] = arr[j++];
    }

    for (i = left; i <= right; ++i)
    {
        arr[i] = temp[i];
    }

    return inv_count;
}

int main()
{
    size_t N;
    std::cin >> N;

    std::vector<unsigned long long> input(N, 0);
    for (auto& x : input)
    {
        std::cin >> x;
    }

    std::cout << mergeSort(input.data(), input.size());
    return 0;
}
