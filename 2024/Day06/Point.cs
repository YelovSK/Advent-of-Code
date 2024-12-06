namespace AoC.Day06;

public readonly struct Point(int x, int y) : IEquatable<Point>
{
    private int X { get; } = x;
    private int Y { get; } = y;

    public bool Equals(Point other)
    {
        return X == other.X && Y == other.Y;
    }

    public override bool Equals(object? obj)
    {
        return obj is Point other && Equals(other);
    }

    public override int GetHashCode()
    {
        return HashCode.Combine(X, Y);
    }
    
    public override string ToString()
    {
        return $"{X}, {Y}";
    }
}