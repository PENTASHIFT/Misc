/* A super simple WAV playback program using ALSA.
   Written to practice using C while writing something productive */

#include <alsa/asoundlib.h>

#define PCM_DEVICE "default"
#define SAMPLE_SIZE (sizeof(short))

typedef struct {
    int sampl_num;
    char *data;
    unsigned int *channels;
} wavdata_t;



snd_pcm_t* AudioOpen(wavdata_t *wavstruct)
{
    snd_pcm_t *handle;
    int err = snd_pcm_open(&handle, PCM_DEVICE, SND_PCM_STREAM_PLAYBACK, 0);
    if (err < 0)
        exit(-1);

    err = snd_pcm_set_params(handle, SND_PCM_FORMAT_S16_LE, SND_PCM_ACCESS_RW_INTERLEAVED, *wavstruct->channels, 44100, 1, 50000);
    
    if (err < 0)
        exit(-1);

    return handle;
}


void wav_init(char *filename, wavdata_t *wavstruct)
{
    const int header_offset = 44;

    FILE *file = fopen(filename, "r");
    if (file == NULL) 
        exit(-1);
    
    fseek(file, 22, SEEK_SET);
    fread(wavstruct->channels, 2, 1, file);

    fseek(file, 0, SEEK_END);
    int size = ftell(file) - header_offset;

    fseek(file, 0, SEEK_SET);
    wavstruct->sampl_num = size / SAMPLE_SIZE;

    wavstruct->data = malloc(size);
    if (wavstruct->data == NULL)
        exit(-1);

    int samplesRead = fread(wavstruct->data, SAMPLE_SIZE, wavstruct->sampl_num, file);
    fclose(file);
}


void wav_play(snd_pcm_t *handle, wavdata_t *wavstruct)
{
    fflush(stdout);
    snd_pcm_uframes_t sampl_num;
    snd_pcm_sframes_t frames = snd_pcm_writei(handle, wavstruct->data, wavstruct->sampl_num);
 
    if (frames < 0)
        frames = snd_pcm_recover(handle, frames, 0);
    if (frames < 0) 
        exit(-1);
}


int main(int argc, char *argv[])
{
    wavdata_t sample;
    wav_init(argv[1], &sample);
    snd_pcm_t *handle = AudioOpen(&sample);
    wav_play(handle, &sample);

    snd_pcm_drain(handle);
    snd_pcm_hw_free(handle);
    snd_pcm_close(handle);
    free(sample.data);

    return 0; 
}
