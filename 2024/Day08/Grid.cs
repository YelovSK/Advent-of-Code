using AoC.Library.Helpers;

namespace AoC.Day08;

public class Grid
{
    public Dictionary<char, List<Position>> Frequencies { get; set; } = new();
    public Size Size { get; set; }
}