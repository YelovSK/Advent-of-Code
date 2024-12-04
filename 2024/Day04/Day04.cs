using AoC.Library;
using AoC.Library.Helpers;

namespace AoC.Day04;

public class Day04 : BaseDay
{
    private readonly string[] PATTERNS = ["XMAS", "SAMX"];
    private readonly string[] X_PATTERNS = ["MAS", "SAM"];

    protected override string Part1(string input)
    {
        var lines = input.SplitLines().ToList();
        return lines
            .SelectMany((line, r) => line.Select((_, c) => (r, c)))
            .Sum(pos => GetPatternCount(lines, pos.r, pos.c))
            .ToString();
    }

    protected override string Part2(string input)
    {
        var lines = input.SplitLines().ToList();
        return lines
            .SelectMany((line, r) => line.Select((_, c) => (r, c)))
            .Count(pos => IsXmas(lines, pos.r, pos.c))
            .ToString();
    }

    protected override string RelativeInputPath => "Day04/input.txt";

    private int GetPatternCount(List<string> lines, int r, int c)
    {
        Utils.TryRun(() => new string(
        [
            lines[r][c],
            lines[r][c + 1],
            lines[r][c + 2],
            lines[r][c + 3]
        ]), out var row);

        Utils.TryRun(() => new string(
        [
            lines[r][c],
            lines[r + 1][c],
            lines[r + 2][c],
            lines[r + 3][c]
        ]), out var col);

        Utils.TryRun(() => new string(
        [
            lines[r][c],
            lines[r + 1][c + 1],
            lines[r + 2][c + 2],
            lines[r + 3][c + 3],
        ]), out var diagonalRight);

        Utils.TryRun(() => new string(
        [
            lines[r][c],
            lines[r + 1][c - 1],
            lines[r + 2][c - 2],
            lines[r + 3][c - 3],
        ]), out var diagonalLeft);

        var matches = 0;

        matches += PATTERNS.Contains(row).ToInt();
        matches += PATTERNS.Contains(col).ToInt();
        matches += PATTERNS.Contains(diagonalRight).ToInt();
        matches += PATTERNS.Contains(diagonalLeft).ToInt();

        return matches;
    }

    private bool IsXmas(List<string> lines, int r, int c)
    {
        Utils.TryRun(() => new string(
        [
            lines[r - 1][c - 1],
            lines[r][c],
            lines[r + 1][c + 1]]
        ), out var diagonalRight);

        Utils.TryRun(() => new string(
        [
            lines[r - 1][c + 1],
            lines[r][c],
            lines[r + 1][c - 1]
        ]), out var diagonalLeft);

        return X_PATTERNS.Contains(diagonalRight) && X_PATTERNS.Contains(diagonalLeft);
    }
}