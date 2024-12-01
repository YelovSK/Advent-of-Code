using System.Text;

namespace AoC.Library;

public class Solution
{
   public TimeSpan Part1Elapsed { get; set; } = TimeSpan.Zero;
   public TimeSpan Part2Elapsed { get; set; } = TimeSpan.Zero;

   public string? Part1Result { get; set; }
   public string? Part2Result { get; set; }
   
   public TimeSpan Elapsed => Part1Elapsed.Add(Part2Elapsed);
   
   public override string ToString()
   {
       var builder = new StringBuilder();

       if (Part1Result != null)
       {
           builder.AppendLine($"PART 1 in {Part1Elapsed.Milliseconds}ms:");
           builder.AppendLine(Part1Result);
       }
       
       if (Part2Result != null)
       {
           builder.AppendLine($"PART 2 in {Part2Elapsed.Milliseconds}ms:");
           builder.AppendLine(Part2Result);
       }
       
       return builder.ToString();
   }
}

public class DaySolution(int day, Solution solution)
{
   public int Day { get; set; } = day;
   public Solution Solution { get; set; } = solution;
}
