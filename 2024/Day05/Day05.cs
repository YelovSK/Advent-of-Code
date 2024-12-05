using AoC.Library;
using AoC.Library.Helpers;

namespace AoC.Day05;

public class Day05 : BaseDay
{
    // Originally checked with regex, like "{after},.*{before}", but this is faster
    protected override string Part1(string input)
    {
        var rulesMap = GetInvalidRulesMap(input);
        var updates = GetUpdates(input);

        var sum = 0;
        foreach (var update in updates)
        {
            var isCorrect = true;

            for (var i = 0; i < update.Count - 1; i++)
            {
                for (var j = i + 1; j < update.Count; j++)
                {
                    var before = update[i];
                    var after = update[j];
                    if (rulesMap.TryGetValue(before, out var beforeRules) && beforeRules.Contains(after))
                    {
                        isCorrect = false;
                        break; // doesn't break out of the outer loop but w/e
                    }
                }
            }

            if (isCorrect) sum += update.Middle();
        }

        return sum.ToString();
    }

    protected override string Part2(string input)
    {
        var rulesMap = GetInvalidRulesMap(input);
        var updates = GetUpdates(input);

        var sum = 0;
        foreach (var update in updates)
        {
            var isCorrect = true;

            for (var i = 0; i < update.Count - 1; i++)
            {
                for (var j = i + 1; j < update.Count; j++)
                {
                    var before = update[i];
                    var after = update[j];
                    if (rulesMap.TryGetValue(before, out var beforeUpdates) && beforeUpdates.Contains(after))
                    {
                        update[i] = after;
                        update[j] = before;
                        isCorrect = false;
                    }
                }
            }

            if (!isCorrect) sum += update.Middle();
        }

        return sum.ToString();
    }

    protected override string RelativeInputPath => "Day05/input.txt";

    /// <returns>[after] -> [before1, before2, ...]</returns>
    private Dictionary<int, List<int>> GetInvalidRulesMap(string input)
    {
        return input
            .Split("\r\n\r\n")[0]
            .SplitLines()
            .Select(line => line.Split('|'))
            .Select(nums => (nums[0].ToInt(), nums[1].ToInt()))
            .GroupBy(rule => rule.Item2)
            .ToDictionary(rule => rule.Key, rule => rule.Select(x => x.Item1).ToList());
    }

    private List<List<int>> GetUpdates(string input)
    {
        return input
            .Split("\r\n\r\n")[1]
            .SplitLines()
            .Select(line => line.Split(',').Select(int.Parse).ToList())
            .ToList();
    }
}