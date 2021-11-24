#!/usr/bin/perl

#
#  Note this file was automacially generated by the GFS
#    prgram make_perl_formatter. You should modified this file
#    only under unusual circumstances.
#

use FindBin qw($Bin);   # Find directory where this script was executed.
use lib "$Bin/../perllib";     # Add library directory to lib path. 
use GFS_format;

parse_args(@ARGV);

sub VALID_DATE {
  TIME_FORMAT("%m%d%y") 

;
}

sub VALID_HOUR {
  FORMAT("%02d", TIME_FORMAT("%H") + 1)

;
}

sub direction_string {
  my $degrees =  shift;
  $degrees eq "  -" ? "  -" :
  $degrees < 22.5 ?  "  N" :
  $degrees < 67.5 ?  " NE" :
  $degrees < 112.5 ? "  E" :
  $degrees < 157.5 ? " SE" :
  $degrees < 202.5 ? "  S" :
  $degrees < 247.5 ? " SW" :
  $degrees < 292.5 ? "  W" :
  $degrees < 337.5 ? " NW" : "  N"

;
}

sub LIGHT_INTENSITY {
  EE_DESCRIPTION(EE_WEATHER("%d", "   ")) ;
}

sub EE_DESCRIPTION {
  my $code =  shift;
  $code eq "0" ? "9" :
$code eq "1" ? "9" :
$code eq "2" ? "6" :
$code eq "3" ? "5" :
$code eq "4" ? "7" :
$code eq "5" ? "4" :
$code eq "6" ? "6" :
$code eq "7" ? "7" :
$code eq "8" ? "7" :
$code eq "9" ? "5" :
$code eq "10" ? "9" :
$code eq "11" ? "1" :
$code eq "12" ? "3" :
$code eq "13" ? "3" :
$code eq "14" ? "2" :
$code eq "15" ? "2" :
$code eq "16" ? "2" :
$code eq "17" ? "3" :
$code eq "18" ? "1" :
$code eq "19" ? "3" :
$code eq "20" ? "3" :
$code eq "21" ? "2" :
$code eq "22" ? "2" :
$code eq "23" ? "2" :
$code eq "24" ? "3" :
$code eq "25" ? "3" :
$code eq "26" ? "3" :
$code eq "27" ? "2" :
$code eq "28" ? "2" :
$code eq "29" ? "2" :
$code eq "30" ? "3" :
$code eq "31" ? "3" :
$code eq "32" ? "3" :
$code eq "33" ? "2" :
$code eq "34" ? "2" :
$code eq "35" ? "2" :
$code eq "36" ? "3" :
$code eq "37" ? "3" :
$code eq "38" ? "3" :
$code eq "39" ? "2" :
$code eq "40" ? "2" :
$code eq "41" ? "3" :
$code eq "42" ? "3" :
$code eq "43" ? "8" :
$code eq "44" ? "7" :
$code eq "45" ? "5" :
$code eq "46" ? "5" :
$code eq "47" ? "9" :
$code eq "48" ? "3" :
$code eq "49" ? "3" :
$code eq "50" ? "2" :
$code eq "51" ? "2" :
$code eq "52" ? "2" :
$code eq "53" ? "3" :
$code eq "54" ? "3" :
$code eq "55" ? "3" :
$code eq "56" ? "2" :
$code eq "57" ? "2" :
$code eq "58" ? "2" :
$code eq "59" ? "3" :
$code eq "60" ? "3" :
$code eq "61" ? "2" :
$code eq "62" ? "3" :
"9"

;
}

sub print_record_USER_EST_TIME {
  send_output SET_TIMEZONE("AmNework");
}

sub print_record_USER_DATA {
  send_output VALID_DATE();
  send_output TEXT(" ");
  send_output VALID_HOUR();
  send_output TEXT(" ");
  send_output STATION_FAA();
  send_output TEXT("   ");
  send_output FORMAT("%1d", LIGHT_INTENSITY());
  send_output TEXT("  ");
  send_output TEMP_F("%3d", "---", STATION_IDX(), TIME_OFFSET() + (1 * 3600));
  send_output TEXT("  ");
  send_output DEW_F("%3d", "---", STATION_IDX(), TIME_OFFSET() + (1 * 3600));
  send_output TEXT("");
  send_output FORMAT("%2s", direction_string(WIND_DIR_D("%3.0f", "  -", STATION_IDX(), TIME_OFFSET() + (1 * 3600))));
  send_output TEXT("-");
  send_output WIND_SPEED_M("%02.0f", "---", STATION_IDX(), TIME_OFFSET() + (1 * 3600));
  send_output TEXT("  ");
  send_output RH("%-3.0f", "---", STATION_IDX(), TIME_OFFSET() + (1 * 3600));
  send_output "\n";
}

sub print_header_1 {
}

sub print_footer_1 {
}

sub generate {
  print_header_1;
  print_record_USER_EST_TIME;
  $start_loop_0 = $min_station_idx;
  $end_loop_0 = $max_station_idx;
  $incr_loop_0 = $step_station_idx;
  if ($incr_loop_0 == 0)
  {
    $end_loop_0 = $start_loop_0 - 1;
  }
  $save_loop_0 = $station_idx;
  for ($station_idx = $start_loop_0;
    $incr_loop_0 > 0 ? $station_idx <= $end_loop_0 : $station_idx >= $end_loop_0;
    $station_idx += $incr_loop_0)
  {
    $start_loop_1 = 0 ;
    $end_loop_1 =  9;
    $incr_loop_1 = $step_LOCAL_DAY;
    if ($incr_loop_1 == 0)
    {
      $end_loop_1 = $start_loop_1 - 1;
    }
    $save_loop_1 = $LOCAL_DAY;
    for ($LOCAL_DAY = $start_loop_1;
      $incr_loop_1 > 0 ? $LOCAL_DAY <= $end_loop_1 : $LOCAL_DAY >= $end_loop_1;
      $LOCAL_DAY += $incr_loop_1)
    {
      $save_time_offset_sec_1 = $time_offset_sec;
      $time_offset_sec = ABSOLUTE_DAY_HOUR($LOCAL_DAY,$LOCAL_HOUR);
      $start_loop_2 = 0 ;
      $end_loop_2 =  23;
      $incr_loop_2 = $step_LOCAL_HOUR;
      if ($incr_loop_2 == 0)
      {
        $end_loop_2 = $start_loop_2 - 1;
      }
      $save_loop_2 = $LOCAL_HOUR;
      for ($LOCAL_HOUR = $start_loop_2;
        $incr_loop_2 > 0 ? $LOCAL_HOUR <= $end_loop_2 : $LOCAL_HOUR >= $end_loop_2;
        $LOCAL_HOUR += $incr_loop_2)
      {
        $save_time_offset_sec_2 = $time_offset_sec;
        $time_offset_sec = ABSOLUTE_DAY_HOUR($LOCAL_DAY,$LOCAL_HOUR);
        print_record_USER_DATA;
        $time_offset_sec = $save_time_offset_sec_2
      }
      $LOCAL_HOUR = $save_loop_2;
      $time_offset_sec = $save_time_offset_sec_1
    }
    $LOCAL_DAY = $save_loop_1;
  }
  $station_idx = $save_loop_0;
  print_footer_1;
}

start_first_pass;
generate;
start_second_pass;
generate;
