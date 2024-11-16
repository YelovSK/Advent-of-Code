namespace AoC.Library;

public class SolveOptions(bool solvePart1, bool solvePart2)
{
    public bool SolvePart1 { get; init; } = solvePart1;
    public bool SolvePart2 { get; init; } = solvePart2;
}