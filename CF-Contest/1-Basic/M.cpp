#include <cmath>
#include <iomanip>
#include <iostream>
#include <utility>

// @return: maximize ? {argmax f(x), max f(x)} : {argmin f(x), min f(x)}
template <typename Fn>
auto optimize_convex(const Fn& f, double xl, double xu, double err, bool maximize = false)
{
    const double phi = (1 + sqrt(5)) / 2;
    const int iter = (log(xu - xl) - log(err)) / log(phi) + 1;

    double xml = (phi * xl + xu) / (1 + phi);
    double xmu = (xl + phi * xu) / (1 + phi);
    double yml = f(xml);
    double ymu = f(xmu);

    for (int i = 0; i < iter; ++i)
    {
        if (!maximize ^ (yml > ymu))
        {
            xu = xmu;
            xmu = xml;
            ymu = yml;
            xml = (phi * xl + xu) / (1 + phi);
            yml = f(xml);
        }
        else
        {
            xl = xml;
            xml = xmu;
            yml = ymu;
            xmu = (xl + phi * xu) / (1 + phi);
            ymu = f(xmu);
        }
    }

    return std::make_pair(xml, yml);
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);

    double v1, v2, a;
    std::cin >> v1 >> v2 >> a;

    double x1 = 0, y1 = 1, x2 = 1, y2 = 0;
    auto func = [&](double x)
    {
        double d1 = sqrt((y1 - a) * (y1 - a) + (x - x1) * (x - x1));
        double t1 = d1 / v1;

        double d2 = sqrt((x2 - x) * (x2 - x) + (a - y2) * (a - y2));
        double t2 = d2 / v2;

        return t1 + t2;
    };

    auto [x, _] = optimize_convex(func, x1, x2, 1e-9, false);
    std::cout << std::setprecision(9) << x << std::endl;

    return 0;
}
