using System.Collections.Concurrent;
using AoC.Library;
using AoC.Library.Helpers;

namespace AoC.Day11;

public class Day11 : BaseDay
{
    protected override string Part1(string input)
    {
        return GetStoneCount(input, 25).ToString();
    }

    protected override string Part2(string input)
    {
        return GetStoneCount(input, 75).ToString();
    }

    protected override string RelativeInputPath => "Day11/input.txt";

    private long GetStoneCount(string input, int blinks)
    {
        var counts = input
            .SplitWords()
            .Select(long.Parse)
            .ToCounter<long, long>()
            .ToConcurrent();

        for (var blink = 0; blink < blinks; blink++)
        {
            var countsNew = new ConcurrentDictionary<long, long>();
            
            // Parallel barely helps, I just wanted to try it.
            Parallel.ForEach(counts, kvp =>
            {
                var (value, count) = kvp;
                var (first, second) = GetStones(value);

                countsNew.AddOrUpdate(first, count, (_, v) => v + count);
                if (second.HasValue)
                {
                    countsNew.AddOrUpdate(second.Value, count, (_, v) => v + count);
                }
            });
            
            counts = countsNew;
        }

        return counts.Values.Sum();
    }

    private (long First, long? Second) GetStones(long value)
    {
        if (value == 0)
        {
            return (1, null);
        }

        var str = value.ToString();
        switch (str.Length % 2)
        {
            case 0:
            {
                var first = str[..(str.Length / 2)].ToLong();
                var second = str[(str.Length / 2)..].ToLong();
                
                return (first, second);
            }
            case 1:
                return (value * 2024, null);
            default:
                throw new ArithmeticException("Not how math works");
        }
    }
}