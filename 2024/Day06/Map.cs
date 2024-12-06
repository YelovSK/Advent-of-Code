namespace AoC.Day06;

public class Map
{
    public HashSet<Point> Obstacles { get; set; } = new();
    public HashSet<Point> Points { get; set; } = new();
    public Guard Guard { get; set; }
    public (int X, int Y) Size { get; set; }
}