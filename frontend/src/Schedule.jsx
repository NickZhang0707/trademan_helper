import * as React from 'react';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import Stack from '@mui/material/Stack';
import Typography from '@mui/material/Typography';
import Copyright from './internals/components/Copyright';
import ChartUserByCountry from './components/ChartUserByCountry';
import CustomizedTreeView from './components/CustomizedTreeView';
import CustomizedDataGrid from './components/CustomizedDataGrid';
import HighlightedCard from './components/HighlightedCard';
import PageViewsBarChart from './components/PageViewsBarChart';
import SessionsChart from './components/SessionsChart';
import StatCard from './components/StatCard';
import Stepper from '@mui/joy/Stepper';
import Step from '@mui/joy/Step';
import StepIndicator from '@mui/joy/StepIndicator';





export default function MainGrid() {
  return (
    <Box sx={{ width: '100%', maxWidth: { sm: '100%', md: '1700px' } }}>
      {/* cards */}
      <Typography component="h2" variant="h6" sx={{ mb: 2 }}>
        Schedule.jsx
      </Typography>
      <Grid
        container
        spacing={2}
        columns={12}
        sx={{ mb: (theme) => theme.spacing(2) }}
      >
        
        <Grid size={{ xs: 12, sm: 6, lg: 3 }}>
          <Typography variant="h6" sx={{ mb: 2 }}>
            Time Line
          </Typography>
        </Grid>
        
        <Grid size={{ xs: 12, sm: 6, lg: 3 }}>
          <HighlightedCard />
        </Grid>
        <Grid size={{ xs: 12, sm: 10 , lg: 10 }}>

          <Stepper sx={{ width: '100%' }}>
            <Step
              indicator={
                <StepIndicator variant="solid" color="neutral">
                  1
                </StepIndicator>
              }
            >
              Surpport Structure
            </Step>
            <Step indicator={<StepIndicator variant="outlined">2</StepIndicator>}>
              Wall
            </Step>
            <Step indicator={<StepIndicator>3</StepIndicator>}>
              Exterior
            </Step>
          </Stepper> 
          
        </Grid>
      </Grid>

      <Typography component="h2" variant="h6" sx={{ mb: 2 }}>
        To Do
      </Typography>
      <Grid container spacing={2} columns={12}>
        <Grid size={{ xs: 12, lg: 9 }}>
          {/* <CustomizedDataGrid /> */}
        </Grid>
      </Grid>

      {/* Copyright */}
      <Copyright sx={{ my: 4 }} />
    </Box>
  );
}
