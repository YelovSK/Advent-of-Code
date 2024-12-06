namespace AoC.Day06;

public class Map
{
    public HashSet<Point> Obstacles { get; set; } = new();
    public HashSet<Point> Points { get; set; } = new();
    public Guard Guard { get; set; }
    public (int, int) Size { get; set; }
}