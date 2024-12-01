using System.Diagnostics;

namespace AoC.Library;

public static class Solver
{
    public static Solution Solve(BaseDay day, SolveOptions options)
    {
        var solution = new Solution();

        if (options.SolvePart1)
        {
            var (result, elapsed) = TimeFunction(day.Part1);
            solution.Part1Result = result;
            solution.Part1Elapsed = elapsed;
        }

        if (options.SolvePart2)
        {
            var (result, elapsed) = TimeFunction(day.Part2);
            solution.Part2Result = result;
            solution.Part2Elapsed = elapsed;
        }

        return solution;
    }

    public static Solution SolvePart1(BaseDay day) => Solve(day, new SolveOptions(true, false));
    public static Solution SolvePart2(BaseDay day) => Solve(day, new SolveOptions(false, true));

    private static (string Result, TimeSpan Elapsed) TimeFunction(Func<string> func)
    {
        var start = Stopwatch.GetTimestamp();

        string result;
        try
        {
            result = func();
        }
        catch (Exception ex)
        {
            result = $"Exception: {ex.Message}";
        }

        return (result, Stopwatch.GetElapsedTime(start));
    }
}