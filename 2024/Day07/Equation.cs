namespace AoC.Day07;

public class Equation(ulong result, List<ulong> operands)
{
    public ulong Result { get; set; } = result;
    public List<ulong> Operands { get; set; } = operands;

    public override string ToString()
    {
        return $"{Result}: {string.Join(" ", Operands)}";
    }
}