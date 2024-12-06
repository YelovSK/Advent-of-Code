namespace AoC.Day06;

public readonly struct GuardState(Point point, (int, int) direction) : IEquatable<GuardState>
{
    public (int, int) Direction { get; } = direction;
    public Point Position { get; } = point;

    public bool Equals(GuardState other)
    {
        return Position.Equals(other.Position) && Direction.Equals(other.Direction);
    }

    public override bool Equals(object? obj)
    {
        return obj is GuardState other && Equals(other);
    }

    public override int GetHashCode()
    {
        return HashCode.Combine(Position, Direction);
    }
}