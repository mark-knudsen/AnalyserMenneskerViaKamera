using System;
using System.Collections.Generic;
using System.Text;

namespace CovidCounter
{
    public class CovidShop
    {
        public int Id { get; set; }
        public string Butiksnavn { get; set; }
        public int Antal { get; set; }
        public int AntalMax {get; set;}


        public CovidShop (int id, String butiksnavn, int antal, int antalMax)
        {
            Id = id;
            Butiksnavn = butiksnavn;
            Antal = antal;
            AntalMax = antalMax;

        }
    }
}
