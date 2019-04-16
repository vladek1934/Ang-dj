import {EventEmitter, Injectable} from '@angular/core';
import {MainService} from './main.service';
import {Task, Tasklist} from '../models/models';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})

export class ProviderService extends MainService {
  constructor(http: HttpClient) {
    super(http);
  }

  getTasklists(): Promise<Tasklist[]> {
    return this.get('http://localhost:8000/api/task_lists', {});
  }

  getTasks(tasklist: Tasklist): Promise<Task[]> {
    return this.get(`http://localhost:8000/api/task_lists/${tasklist.id}/tasks`, {});
  }

  getTask(id: number): Promise<Task> {
    return this.get(`http://localhost:8000/api/tasks/${id}`, {});
  }
}


